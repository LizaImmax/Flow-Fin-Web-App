from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    
    smart_home_entries = db.relationship('SmartHomeEntry', backref='user', lazy=True)
    connected_car_entries = db.relationship('ConnectedCarEntry', backref='user', lazy=True)
    health_tracker_entries = db.relationship('HealthTrackerEntry', backref='user', lazy=True)
    grocery_shopping_entries = db.relationship('GroceryShoppingEntry', backref='user', lazy=True)
    wearable_finance_entries = db.relationship('WearableFinanceEntry', backref='user', lazy=True)
    financial_entries = db.relationship('FinancialEntry', backref='user', lazy=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

class SmartHomeEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    entry_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    # Add other fields related to Smart Home Finance Manager
    
    def __init__(self, user_id, entry_date):
        self.user_id = user_id
        self.entry_date = entry_date

class ConnectedCarEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    entry_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    # Add other fields related to Connected Car Finance Hub
    
    def __init__(self, user_id, entry_date):
        self.user_id = user_id
        self.entry_date = entry_date

class HealthTrackerEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    entry_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    # Add other fields related to Health Tracker Insurance Integration
    
    def __init__(self, user_id, entry_date):
        self.user_id = user_id
        self.entry_date = entry_date

class GroceryShoppingEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    entry_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    # Add other fields related to Grocery Shopping Budget Optimizer
    
    def __init__(self, user_id, entry_date):
        self.user_id = user_id
        self.entry_date = entry_date

class WearableFinanceEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    entry_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    # Add other fields related to Wearable Finance Assistant
    
    def __init__(self, user_id, entry_date):
        self.user_id = user_id
        self.entry_date = entry_date

class FinancialEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    entry_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    # Add other fields related to general financial entries
    
    def __init__(self, user_id, entry_date):
        self.user_id = user_id
        self.entry_date = entry_date

# Initialize the database
def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
