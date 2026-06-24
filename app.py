import os
import random
from datetime import date, timedelta

from flask import Flask, jsonify, request, send_from_directory, render_template

from models import (
    db,
    Recipe,
    Ingredient,
    RecipeIngredient,
    Tag,
    WeeklyPlan,
    WeeklyPlanMeal,
    GroceryList,
    GroceryListItem,
    DAY_NAMES,
    CATEGORY_ORDER,
)


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dinner_deck.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()

    register_routes(app)
    return app


def register_routes(app):
    @app.route("/")
    def index():
        return render_template("index.html")

    # ---- PWA passthrough (must be served from root scope) ----
    @app.route("/manifest.json")
    def manifest():
        return send_from_directory("static", "manifest.json")

    @app.route("/sw.js")
    def service_worker():
        return send_from_directory("static/js", "sw.js")

    # ---- Recipes ----
    @app.route("/api/recipes", methods=["GET"])
    def list_recipes():
        cuisine = request.args.get("cuisine")
        exclude_tags = request.args.getlist("exclude_tag")
        max_cook_time = request.args.get("max_cook_time", type=int)

        query = Recipe.query
        if cuisine:
            query = query.filter_by(cuisine_type=cuisine)
        if max_cook_time:
            query = query.filter(Recipe.cook_time_minutes <= max_cook_time)

        recipes = query.all()
        if exclude_tags:
            exclude_set = set(exclude_tags)
            recipes = [r for r in recipes if not exclude_set & {t.name for t in r.tags}]

        return jsonify([r.to_dict() for r in recipes])

    @app.route("/api/recipes/<int:recipe_id>", methods=["GET"])
    def get_recipe(recipe_id):
        recipe = Recipe.query.get_or_404(recipe_id)
        return jsonify(recipe.to_dict())

    @app.route("/api/recipes", methods=["POST"])
    def create_recipe():
        data = request.get_json()
        recipe = _build_recipe_from_payload(data)
        db.session.add(recipe)
        db.session.commit()
        return jsonify(recipe.to_dict()), 201

    @app.route("/api/recipes/<int:recipe_id>", methods=["PUT"])
    def update_recipe(recipe_id):
        recipe = Recipe.query.get_or_404(recipe_id)
        data = request.get_json()

        recipe.name = data["name"]
        recipe.cuisine_type = data["cuisine_type"]
        recipe.cook_time_minutes = data["cook_time_minutes"]
        recipe.base_servings = data.get("base_servings", recipe.base_servings)
        recipe.instructions = data.get("instructions", recipe.instructions)

        recipe.ingredients = []
        recipe.tags = []
        db.session.flush()
        _apply_ingredients_and_tags(recipe, data)

        db.session.commit()
        return jsonify(recipe.to_dict())

    @app.route("/api/recipes/<int:recipe_id>", methods=["DELETE"])
    def delete_recipe(recipe_id):
        recipe = Recipe.query.get_or_404(recipe_id)
        db.session.delete(recipe)
        db.session.commit()
        return "", 204

    @app.route("/api/tags", methods=["GET"])
    def list_tags():
        return jsonify([t.name for t in Tag.query.all()])

    # ---- Weekly plan (meal generator) ----
    @app.route("/api/plans/generate", methods=["POST"])
    def generate_plan():
        data = request.get_json() or {}
        exclude_tags = set(data.get("exclude_tags", []))
        week_start = data.get("week_start_date")
        week_start_date = date.fromisoformat(week_start) if week_start else _next_monday()

        pool = Recipe.query.all()
        if exclude_tags:
            pool = [r for r in pool if not exclude_tags & {t.name for t in r.tags}]
        if len(pool) < 5:
            return jsonify({"error": "Not enough recipes left after exclusions"}), 400

        chosen = random.sample(pool, 5)

        plan = WeeklyPlan(week_start_date=week_start_date)
        db.session.add(plan)
        db.session.flush()

        for day_of_week, recipe in enumerate(chosen):
            db.session.add(
                WeeklyPlanMeal(weekly_plan_id=plan.id, recipe_id=recipe.id, day_of_week=day_of_week)
            )

        db.session.commit()
        return jsonify(_plan_to_dict(plan)), 201

    @app.route("/api/plans/<int:plan_id>", methods=["GET"])
    def get_plan(plan_id):
        plan = WeeklyPlan.query.get_or_404(plan_id)
        return jsonify(_plan_to_dict(plan))

    @app.route("/api/plans/latest", methods=["GET"])
    def latest_plan():
        plan = WeeklyPlan.query.order_by(WeeklyPlan.created_at.desc()).first()
        if not plan:
            return jsonify(None)
        return jsonify(_plan_to_dict(plan))

    @app.route("/api/plans/<int:plan_id>/meals/<int:meal_id>", methods=["PUT"])
    def update_plan_meal(plan_id, meal_id):
        meal = WeeklyPlanMeal.query.filter_by(id=meal_id, weekly_plan_id=plan_id).first_or_404()
        data = request.get_json()
        if "recipe_id" in data:
            meal.recipe_id = data["recipe_id"]
        if "servings_override" in data:
            meal.servings_override = data["servings_override"]
        db.session.commit()
        return jsonify(_meal_to_dict(meal))

    # ---- Grocery list ----
    @app.route("/api/plans/<int:plan_id>/grocery-list", methods=["POST"])
    def generate_grocery_list(plan_id):
        plan = WeeklyPlan.query.get_or_404(plan_id)

        if plan.grocery_list:
            db.session.delete(plan.grocery_list)
            db.session.flush()

        totals = {}  # (ingredient_id, unit) -> amount
        for meal in plan.meals:
            scale = meal.servings / meal.recipe.base_servings
            for ri in meal.recipe.ingredients:
                key = (ri.ingredient_id, ri.unit)
                totals[key] = totals.get(key, 0) + ri.amount * scale

        grocery_list = GroceryList(weekly_plan_id=plan.id)
        db.session.add(grocery_list)
        db.session.flush()

        for (ingredient_id, unit), amount in totals.items():
            db.session.add(
                GroceryListItem(
                    grocery_list_id=grocery_list.id,
                    ingredient_id=ingredient_id,
                    total_amount=round(amount, 2),
                    unit=unit,
                )
            )

        db.session.commit()
        return jsonify(_grocery_list_to_dict(grocery_list)), 201

    @app.route("/api/grocery-lists/<int:list_id>/items/<int:item_id>", methods=["PUT"])
    def toggle_grocery_item(list_id, item_id):
        item = GroceryListItem.query.filter_by(id=item_id, grocery_list_id=list_id).first_or_404()
        data = request.get_json()
        item.checked = data.get("checked", item.checked)
        db.session.commit()
        return jsonify(_item_to_dict(item))


def _next_monday():
    today = date.today()
    return today + timedelta(days=(7 - today.weekday()) % 7 or 7)


def _build_recipe_from_payload(data):
    recipe = Recipe(
        name=data["name"],
        cuisine_type=data["cuisine_type"],
        cook_time_minutes=data["cook_time_minutes"],
        base_servings=data.get("base_servings", 4),
        instructions=data.get("instructions"),
    )
    db.session.add(recipe)
    db.session.flush()
    _apply_ingredients_and_tags(recipe, data)
    return recipe


def _apply_ingredients_and_tags(recipe, data):
    for item in data.get("ingredients", []):
        ingredient = _get_or_create_ingredient(item["ingredient"])
        recipe.ingredients.append(
            RecipeIngredient(ingredient_id=ingredient.id, amount=item["amount"], unit=item["unit"])
        )
    for tag_name in data.get("tags", []):
        recipe.tags.append(_get_or_create_tag(tag_name))


def _get_or_create_ingredient(name):
    name = name.strip().lower()
    ingredient = Ingredient.query.filter_by(name=name).first()
    if not ingredient:
        ingredient = Ingredient(name=name)
        db.session.add(ingredient)
        db.session.flush()
    return ingredient


def _get_or_create_tag(name):
    name = name.strip().lower()
    tag = Tag.query.filter_by(name=name).first()
    if not tag:
        tag = Tag(name=name)
        db.session.add(tag)
        db.session.flush()
    return tag


def _meal_to_dict(meal):
    return {
        "id": meal.id,
        "day_of_week": meal.day_of_week,
        "day_name": DAY_NAMES[meal.day_of_week],
        "servings": meal.servings,
        "recipe": meal.recipe.to_dict(servings=meal.servings),
    }


def _plan_to_dict(plan):
    return {
        "id": plan.id,
        "week_start_date": plan.week_start_date.isoformat(),
        "meals": [_meal_to_dict(m) for m in plan.meals],
        "grocery_list_id": plan.grocery_list.id if plan.grocery_list else None,
    }


def _item_to_dict(item):
    return {
        "id": item.id,
        "ingredient": item.ingredient.name,
        "category": item.ingredient.category,
        "amount": item.total_amount,
        "unit": item.unit,
        "checked": item.checked,
    }


def _category_sort_key(item_dict):
    try:
        category_rank = CATEGORY_ORDER.index(item_dict["category"])
    except ValueError:
        category_rank = len(CATEGORY_ORDER)
    return (category_rank, item_dict["ingredient"])


def _grocery_list_to_dict(grocery_list):
    items = sorted([_item_to_dict(i) for i in grocery_list.items], key=_category_sort_key)
    return {
        "id": grocery_list.id,
        "weekly_plan_id": grocery_list.weekly_plan_id,
        "generated_at": grocery_list.generated_at.isoformat(),
        "items": items,
    }


app = create_app()

if __name__ == "__main__":
    host = os.environ.get("FLASK_HOST", "0.0.0.0")
    debug = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
    app.run(host=host, port=5050, debug=debug)
