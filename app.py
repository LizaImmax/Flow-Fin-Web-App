from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, login_required, logout_user, current_user
from basemodel import RegistrationForm, UserProfileForm, SmartHomeForm, ConnectedCarForm, HealthTrackerForm, GroceryShoppingForm, WearableFinanceForm
from config import app, db, bcrypt, login_manager  
from models.connected_car import ConnectedCar
from models.grocery_shopping import GroceryShopping
from models.health_tracker import HealthTracker
from models.wearable_finance import WearableFinance
from models.smart_home import SmartHome
from models.user import User

app = Flask(__name__)

# Home Page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup' , methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')

# Login page
@app.route('/login')
def login():
    return render_template('login.html')

# Financial Component Routes
@app.route('/smart_home')
def smart_home():
    return render_template('smart_home.html')

@app.route('/connected_car')
def connected_car():
    return render_template('connected_car.html')

@app.route('/health_tracker')
def health_tracker():
    return render_template('health_tracker.html')

@app.route('/grocery_shopping')
def grocery_shopping():
    return render_template('grocery_shopping.html')

@app.route('/wearable_finance')
def wearable_finance():
    return render_template('wearable_finance.html')

# Additional Template Routes
@app.route('/transaction_history')
def transaction_history():
    return render_template('transaction_history.html')

@app.route('/expense_tracking')
def expense_tracking():
    return render_template('expense_tracking.html')

@app.route('/budgeting_tools')
def budgeting_tools():
    return render_template('budgeting_tools.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/profile_settings')
def profile_settings():
    return render_template('profile_settings.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

# 404 Error Page
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.route('/logout')
@login_required
def logout():
    logout_user()  # Logs the user out
    return redirect(url_for('login'))  # Redirect to the login page or any other desired page


if __name__ == '__main__':
    app.run(debug=True)
