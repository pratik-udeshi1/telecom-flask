from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.fields.core import SelectField
from wtforms.validators import DataRequired, Email, ValidationError, Length


class RegistrationForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    dob = StringField('dob', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    aadhar_number = StringField('aadhar_number', validators=[Length(min=12, max=12)])
    registration_date = StringField('registration_date', default=datetime.now)
    mobile_number = StringField('mobile_number', validators=[Length(min=10, max=10)])
    plan = SelectField('plan', choices=[('Platinum365', 'Platinum365'), ('Gold180', 'Gold180'),
                                        ('Silver90', 'Silver90')], validators=[DataRequired()])

    def validate_dob(self, field):
        try:
            # Parse the date string to a datetime object
            dob_date = datetime.strptime(field.data, '%d-%m-%Y')
        except ValueError:
            raise ValidationError('Invalid date format. Please use dd-mm-yyyy.')

    def validate_aadhar_number(self, field):
        if not field.data.isdigit():
            raise ValidationError('Aadhar number must contain only digits.')


class UserPlanUpgrade(FlaskForm):
    plan = SelectField('plan', choices=[('Platinum365', 'Platinum365'), ('Gold180', 'Gold180'),
                                        ('Silver90', 'Silver90')], validators=[DataRequired()])
