from datetime import datetime, date

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DAY_NAMES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

CATEGORY_ORDER = [
    "Produce",
    "Meat & Seafood",
    "Dairy & Eggs",
    "Bread & Bakery",
    "Frozen",
    "Canned & Jarred Goods",
    "Grains & Pasta",
    "Condiments & Sauces",
    "Spices & Seasonings",
    "Pantry & Dry Goods",
    "Other",
]


recipe_tags = db.Table(
    "recipe_tags",
    db.Column("recipe_id", db.Integer, db.ForeignKey("recipe.id"), primary_key=True),
    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id"), primary_key=True),
)


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    cuisine_type = db.Column(db.String(60), nullable=False)
    cook_time_minutes = db.Column(db.Integer, nullable=False)
    base_servings = db.Column(db.Integer, nullable=False, default=4)
    instructions = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    ingredients = db.relationship(
        "RecipeIngredient", backref="recipe", cascade="all, delete-orphan"
    )
    tags = db.relationship("Tag", secondary=recipe_tags, backref="recipes")

    def to_dict(self, servings=None):
        scale = (servings / self.base_servings) if servings else 1.0
        return {
            "id": self.id,
            "name": self.name,
            "cuisine_type": self.cuisine_type,
            "cook_time_minutes": self.cook_time_minutes,
            "base_servings": self.base_servings,
            "servings": servings or self.base_servings,
            "instructions": self.instructions,
            "tags": [t.name for t in self.tags],
            "ingredients": [
                {
                    "ingredient": ri.ingredient.name,
                    "amount": round(ri.amount * scale, 2),
                    "unit": ri.unit,
                }
                for ri in self.ingredients
            ],
        }


class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, unique=True)
    default_unit = db.Column(db.String(30))
    category = db.Column(db.String(40), nullable=False, default="Other")


class RecipeIngredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipe.id"), nullable=False)
    ingredient_id = db.Column(db.Integer, db.ForeignKey("ingredient.id"), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    unit = db.Column(db.String(30), nullable=False)

    ingredient = db.relationship("Ingredient")


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False, unique=True)


class WeeklyPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    week_start_date = db.Column(db.Date, nullable=False, default=date.today)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    active = db.Column(db.Boolean, nullable=False, default=True)

    meals = db.relationship(
        "WeeklyPlanMeal", backref="plan", cascade="all, delete-orphan",
        order_by="WeeklyPlanMeal.day_of_week",
    )
    grocery_list = db.relationship(
        "GroceryList", backref="plan", uselist=False, cascade="all, delete-orphan"
    )


class WeeklyPlanMeal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weekly_plan_id = db.Column(db.Integer, db.ForeignKey("weekly_plan.id"), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipe.id"), nullable=False)
    day_of_week = db.Column(db.Integer, nullable=False)  # 0=Monday ... 4=Friday
    servings_override = db.Column(db.Integer)  # null => use recipe.base_servings

    recipe = db.relationship("Recipe")

    @property
    def servings(self):
        return self.servings_override or self.recipe.base_servings


class GroceryList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weekly_plan_id = db.Column(
        db.Integer, db.ForeignKey("weekly_plan.id"), nullable=False, unique=True
    )
    generated_at = db.Column(db.DateTime, default=datetime.utcnow)

    items = db.relationship(
        "GroceryListItem", backref="grocery_list", cascade="all, delete-orphan"
    )


class GroceryListItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    grocery_list_id = db.Column(db.Integer, db.ForeignKey("grocery_list.id"), nullable=False)
    ingredient_id = db.Column(db.Integer, db.ForeignKey("ingredient.id"), nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    unit = db.Column(db.String(30), nullable=False)
    checked = db.Column(db.Boolean, default=False)

    ingredient = db.relationship("Ingredient")
