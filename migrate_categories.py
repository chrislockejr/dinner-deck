import sqlite3

from app import create_app
from models import db, Ingredient

CATEGORY_MAP = {
    # Produce
    "apple": "Produce",
    "avocado": "Produce",
    "basil": "Produce",
    "bean sprouts": "Produce",
    "bell pepper": "Produce",
    "bok choy": "Produce",
    "broccoli": "Produce",
    "cabbage": "Produce",
    "carrot": "Produce",
    "celery": "Produce",
    "cherry tomato": "Produce",
    "cilantro": "Produce",
    "corn": "Produce",
    "cucumber": "Produce",
    "garlic": "Produce",
    "ginger": "Produce",
    "green beans": "Produce",
    "green onion": "Produce",
    "lemon": "Produce",
    "lettuce": "Produce",
    "lime": "Produce",
    "onion": "Produce",
    "parsley": "Produce",
    "potato": "Produce",
    "romaine lettuce": "Produce",
    "spinach": "Produce",
    "tomato": "Produce",
    "zucchini": "Produce",
    # Meat & Seafood
    "bacon": "Meat & Seafood",
    "chicken breast": "Meat & Seafood",
    "chicken sausage": "Meat & Seafood",
    "chicken thighs": "Meat & Seafood",
    "cod fillet": "Meat & Seafood",
    "flank steak": "Meat & Seafood",
    "ground beef": "Meat & Seafood",
    "ground turkey": "Meat & Seafood",
    "pork chops": "Meat & Seafood",
    "pork tenderloin": "Meat & Seafood",
    "salmon fillet": "Meat & Seafood",
    "shrimp": "Meat & Seafood",
    "sirloin steak": "Meat & Seafood",
    "tilapia fillet": "Meat & Seafood",
    # Dairy & Eggs
    "butter": "Dairy & Eggs",
    "cheddar cheese": "Dairy & Eggs",
    "egg": "Dairy & Eggs",
    "feta cheese": "Dairy & Eggs",
    "milk": "Dairy & Eggs",
    "mozzarella cheese": "Dairy & Eggs",
    "parmesan cheese": "Dairy & Eggs",
    "tzatziki": "Dairy & Eggs",
    # Bread & Bakery
    "burger buns": "Bread & Bakery",
    "phyllo dough": "Bread & Bakery",
    "pita bread": "Bread & Bakery",
    "tortillas": "Bread & Bakery",
    "tostada shells": "Bread & Bakery",
    # Grains & Pasta
    "chow mein noodles": "Grains & Pasta",
    "couscous": "Grains & Pasta",
    "egg noodles": "Grains & Pasta",
    "lo mein noodles": "Grains & Pasta",
    "macaroni": "Grains & Pasta",
    "orzo": "Grains & Pasta",
    "pasta": "Grains & Pasta",
    "rice": "Grains & Pasta",
    "rice noodles": "Grains & Pasta",
    "soba noodles": "Grains & Pasta",
    "spaghetti": "Grains & Pasta",
    "ziti pasta": "Grains & Pasta",
    "tortilla chips": "Grains & Pasta",
    "croutons": "Grains & Pasta",
    "breadcrumbs": "Grains & Pasta",
    # Canned & Jarred Goods
    "black beans": "Canned & Jarred Goods",
    "chickpeas": "Canned & Jarred Goods",
    "canned tuna": "Canned & Jarred Goods",
    "chicken broth": "Canned & Jarred Goods",
    "enchilada sauce": "Canned & Jarred Goods",
    "kidney beans": "Canned & Jarred Goods",
    "olives": "Canned & Jarred Goods",
    "pinto beans": "Canned & Jarred Goods",
    "tomato sauce": "Canned & Jarred Goods",
    "vegetable broth": "Canned & Jarred Goods",
    "white beans": "Canned & Jarred Goods",
    "hummus": "Canned & Jarred Goods",
    "salsa": "Canned & Jarred Goods",
    # Condiments & Sauces
    "bbq sauce": "Condiments & Sauces",
    "caesar dressing": "Condiments & Sauces",
    "fish sauce": "Condiments & Sauces",
    "honey": "Condiments & Sauces",
    "ketchup": "Condiments & Sauces",
    "mayonnaise": "Condiments & Sauces",
    "mustard": "Condiments & Sauces",
    "olive oil": "Condiments & Sauces",
    "peanut butter": "Condiments & Sauces",
    "peanut sauce": "Condiments & Sauces",
    "rice vinegar": "Condiments & Sauces",
    "sesame oil": "Condiments & Sauces",
    "soy sauce": "Condiments & Sauces",
    "sriracha": "Condiments & Sauces",
    # Spices & Seasonings
    "black pepper": "Spices & Seasonings",
    "brown sugar": "Spices & Seasonings",
    "chili powder": "Spices & Seasonings",
    "cornstarch": "Spices & Seasonings",
    "cumin": "Spices & Seasonings",
    "oregano": "Spices & Seasonings",
    "taco seasoning": "Spices & Seasonings",
    # Nuts, Snacks & Other Pantry
    "cashews": "Pantry & Dry Goods",
    "falafel mix": "Pantry & Dry Goods",
    "peanuts": "Pantry & Dry Goods",
    # Frozen
    "edamame": "Frozen",
    "frozen dumplings": "Frozen",
    "frozen peas and carrots": "Frozen",
    "tofu": "Frozen",
}

def ensure_column(app):
    db_path = app.config["SQLALCHEMY_DATABASE_URI"].replace("sqlite:///", "")
    with app.app_context():
        full_path = db.engine.url.database
    conn = sqlite3.connect(full_path)
    cols = [row[1] for row in conn.execute("PRAGMA table_info(ingredient)")]
    if "category" not in cols:
        conn.execute("ALTER TABLE ingredient ADD COLUMN category VARCHAR(40) DEFAULT 'Other'")
        conn.commit()
    conn.close()


def categorize():
    app = create_app()
    ensure_column(app)

    with app.app_context():
        updated = 0
        uncategorized = []
        for ingredient in Ingredient.query.all():
            category = CATEGORY_MAP.get(ingredient.name)
            if category:
                ingredient.category = category
                updated += 1
            else:
                uncategorized.append(ingredient.name)
        db.session.commit()
        print(f"Categorized {updated} ingredients.")
        if uncategorized:
            print(f"No mapping found for: {uncategorized}")


if __name__ == "__main__":
    categorize()
