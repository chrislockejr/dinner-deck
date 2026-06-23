from app import create_app
from models import db, Recipe
from seed_data import RECIPES


def seed():
    app = create_app()
    with app.app_context():
        existing_names = {r.name for r in Recipe.query.all()}
        added = 0

        for data in RECIPES:
            if data["name"] in existing_names:
                continue

            from app import _build_recipe_from_payload

            recipe = _build_recipe_from_payload(data)
            db.session.add(recipe)
            added += 1

        db.session.commit()
        print(f"Added {added} new recipes ({len(RECIPES) - added} already present).")


if __name__ == "__main__":
    seed()
