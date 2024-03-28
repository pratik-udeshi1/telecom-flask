from flask import (
    Blueprint, request, jsonify,
)
from psycopg2 import IntegrityError

from core.user.forms import RegistrationForm, UserPlanUpgrade
from core.user.models import db, User, Plan

user_bp = Blueprint('user', __name__)


@user_bp.route('/user/register', methods=['POST'])
def register_user():
    data = request.json
    form = RegistrationForm(data=data)
    if form.validate():
        try:
            selected_plan_name = form.plan.data
            selected_plan = Plan.query.filter_by(plan_name=selected_plan_name).first()

            # Create a new user instance
            new_user = User()
            form.populate_obj(new_user)
            new_user.plan = selected_plan
            db.session.add(new_user)
            db.session.commit()
            return jsonify({'message': 'User registered successfully', 'user': new_user.as_dict()}), 201
        except IntegrityError:
            db.session.rollback()
            return jsonify({'message': 'User with provided email, aadhar number, or mobile number already exists'}), 400
    else:
        errors = form.errors
        return jsonify({'message': 'Form validation errors', 'errors': errors}), 400


@user_bp.route('/users', methods=['GET'])
def get_all_users():
    try:
        users = User.query.all()
        users_data = [user.as_dict() for user in users]
        return jsonify(users_data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@user_bp.route('/user/<user_id>/plan', methods=['PATCH'])
def upgrade_user_plan(user_id):
    try:
        # Get the user to upgrade by its ID
        user = User.query.get(user_id)
        if not user:
            return jsonify({'message': 'User not found'}), 404

        form = UserPlanUpgrade(request.form)

        if form.validate():
            selected_plan_name = form.plan.data
            selected_plan = Plan.query.filter_by(plan_name=selected_plan_name).first()
            if not selected_plan:
                return jsonify({'message': 'Plan not found'}), 404

            user.plan = selected_plan
            db.session.commit()
            return jsonify({'message': 'User plan upgraded successfully', 'user': user.as_dict()}), 200
        else:
            errors = form.errors
            return jsonify({'message': 'Form validation errors', 'errors': errors}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
