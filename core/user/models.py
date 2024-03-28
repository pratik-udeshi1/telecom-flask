import uuid
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.String(36), primary_key=True, unique=True, nullable=False, default=lambda: str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    deleted_at = db.Column(db.DateTime, nullable=True)


class User(BaseModel):
    name = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    aadhar_number = db.Column(db.String(12), unique=True, nullable=False)
    registration_date = db.Column(db.String(10), nullable=False)
    mobile_number = db.Column(db.String(10), unique=True, nullable=False)
    plan_id = db.Column(db.String(36), db.ForeignKey('plan.id'), nullable=False)
    plan = relationship('Plan', backref='users')

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Plan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plan_name = db.Column(db.String(100), unique=True, nullable=False)
    plan_cost = db.Column(db.Float, nullable=False)
    plan_validity = db.Column(db.Integer, nullable=False)
    plan_status = db.Column(db.Boolean(), default=True, nullable=False)
