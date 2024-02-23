from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class SmartHome(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    energy_goal = db.Column(db.Integer, nullable=False)
    target_device = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    end_date = db.Column(db.Date, nullable=False, default=datetime.utcnow)

    # Additional fields or relationships for the SmartHome model can be added here.

    def __init__(self, energy_goal, target_device, start_date, end_date):
        self.energy_goal = energy_goal
        self.target_device = target_device
        self.start_date = start_date
        self.end_date = end_date
