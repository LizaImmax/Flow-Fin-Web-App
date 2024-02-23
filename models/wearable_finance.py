from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class WearableFinance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    preferred_categories = db.Column(db.String(200), nullable=False)
    daily_budget = db.Column(db.Float, nullable=False)

    def __init__(self, preferred_categories, daily_budget):
        self.preferred_categories = preferred_categories
        self.daily_budget = daily_budget
