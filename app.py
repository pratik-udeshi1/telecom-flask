from flask import Flask, jsonify
from flask_migrate import Migrate
from sqlalchemy.exc import IntegrityError

from core.user.models import db
from core.user.views import user_bp

app = Flask(__name__)

app.config['SECRET_KEY'] = 'random_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///telecom.db'
app.config['WTF_CSRF_ENABLED'] = False

db.init_app(app)
migrate = Migrate(app, db, render_as_batch=True)

app.register_blueprint(user_bp)


@app.errorhandler(IntegrityError)
def handle_integrity_error(e):
    error_message = "A user with the provided mobile number already exists."
    return jsonify({'message': str(e).split('\n')[0]}), 400


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
