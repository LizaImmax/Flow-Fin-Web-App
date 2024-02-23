from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, IntegerField, DateField
from wtforms.validators import DataRequired, Length, Email

class RegistrationForm(FlaskForm):
    """ Registration method to allow user creat an account.
    Validates if the account meets the requirements, and creates the account

    Args:
        FlaskForm (_type_): _Flask Object to process user login_

    Raises:
        ValidationError: _Raises a validation error when the user registers
        with an email existing in the db_
    """
    username = StringField('Username', validators=[DataRequired()],
                        render_kw={"placeholder": "Username"})
    email = StringField('Email', validators=[DataRequired(), Email()],
                        render_kw={"placeholder": "email"})
    
    password = PasswordField('Password', validators=[DataRequired(),
                                         Length(min=6, max=20)],
                                    render_kw={"placeholder": "password"})
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')],
                                    render_kw={"placeholder": "confirm password"})
    submit = SubmitField("Register")

    def validate_email(self, email):
        """validate user account creation by checking if email exists already

        Args:
            email (_type_): _parameter to check_

        Raises:
            ValidationError: _The error to raise if email exists_
        """
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('The email address is registered, log in or register with another email')
        

class UserProfileForm(FlaskForm):
    full_name = StringField('Full Name', validators=[DataRequired(), Length(max=50)])
    bio = TextAreaField('Bio', validators=[Length(max=250)])
    submit = SubmitField('Update Profile')

class SmartHomeForm(FlaskForm):
    energy_goal = IntegerField('Energy Goal', validators=[DataRequired()])
    target_device = StringField('Target Device', validators=[DataRequired()])
    start_date = DateField('Start Date', format='%Y-%m-%d', validators=[DataRequired()])
    end_date = DateField('End Date', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Create Smart Home Goal')

class ConnectedCarForm(FlaskForm):
    car_model = StringField('Car Model', validators=[DataRequired()])
    year = IntegerField('Year', validators=[DataRequired()])
    fuel_type = StringField('Fuel Type', validators=[DataRequired()])
    submit = SubmitField('Add Connected Car')

class HealthTrackerForm(FlaskForm):
    weight = IntegerField('Weight (kg)', validators=[DataRequired()])
    height = IntegerField('Height (cm)', validators=[DataRequired()])
    blood_pressure = StringField('Blood Pressure', validators=[DataRequired()])
    submit = SubmitField('Record Health Data')

class GroceryShoppingForm(FlaskForm):
    budget = IntegerField('Budget', validators=[DataRequired()])
    store_preference = StringField('Store Preference', validators=[DataRequired()])
    submit = SubmitField('Set Budget and Preferences')

class WearableFinanceForm(FlaskForm):
    preferred_categories = StringField('Preferred Categories', validators=[DataRequired()])
    daily_budget = IntegerField('Daily Budget', validators=[DataRequired()])
    submit = SubmitField('Update Wearable Finance Settings')
