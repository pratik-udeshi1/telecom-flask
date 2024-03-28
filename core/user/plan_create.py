# Assuming you have already defined your Flask app, SQLAlchemy db, and Plan model
from app import app
from core.user.models import Plan, db, User


# Create and add custom plan entries
def add_custom_plans():
    # Define your custom plans
    plans_data = [
        {'plan_name': 'Platinum365', 'plan_cost': 499.0, 'plan_validity': 365, 'plan_status': True},
        {'plan_name': 'Gold180', 'plan_cost': 299.0, 'plan_validity': 180, 'plan_status': True},
        {'plan_name': 'Silver90', 'plan_cost': 199.0, 'plan_validity': 90, 'plan_status': True}
    ]

    # Add custom plans to the database
    for plan_data in plans_data:
        plan = Plan(**plan_data)
        db.session.add(plan)

    # Commit the changes to the database
    db.session.commit()


# Check if plans exist in the database, if not, add them
def check_and_add_plans():
    all_plans = Plan.query.all()

    if not Plan.query.all():
        add_custom_plans()


if __name__ == '__main__':
    # Initialize database
    with app.app_context():
        db.create_all()
        check_and_add_plans()
