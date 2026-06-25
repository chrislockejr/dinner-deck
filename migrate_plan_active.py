import sqlite3

from app import create_app
from models import db, Recipe, WeeklyPlan, WeeklyPlanMeal


def ensure_column(app):
    with app.app_context():
        full_path = db.engine.url.database
    conn = sqlite3.connect(full_path)
    cols = [row[1] for row in conn.execute("PRAGMA table_info(weekly_plan)")]
    if "active" not in cols:
        conn.execute("ALTER TABLE weekly_plan ADD COLUMN active BOOLEAN DEFAULT 1")
        conn.commit()
    conn.close()


def cleanup_orphaned_meals():
    """Remove WeeklyPlanMeal rows whose recipe was deleted, and any grocery
    list left over for a plan affected by that removal."""
    valid_recipe_ids = {r.id for r in Recipe.query.all()}
    orphaned = [m for m in WeeklyPlanMeal.query.all() if m.recipe_id not in valid_recipe_ids]
    affected_plan_ids = {m.weekly_plan_id for m in orphaned}
    for meal in orphaned:
        db.session.delete(meal)
    for plan_id in affected_plan_ids:
        plan = db.session.get(WeeklyPlan, plan_id)
        if plan and plan.grocery_list:
            db.session.delete(plan.grocery_list)
    db.session.commit()
    print(f"Removed {len(orphaned)} orphaned meal(s) across {len(affected_plan_ids)} plan(s).")


def set_one_active_plan():
    """Mark only the most recently created plan as active; all others inactive."""
    plans = WeeklyPlan.query.order_by(WeeklyPlan.created_at.desc()).all()
    for i, plan in enumerate(plans):
        plan.active = (i == 0)
    db.session.commit()
    print(f"Marked plan {plans[0].id if plans else None} as the active plan ({len(plans)} total).")


def migrate():
    app = create_app()
    ensure_column(app)

    with app.app_context():
        cleanup_orphaned_meals()
        set_one_active_plan()


if __name__ == "__main__":
    migrate()
