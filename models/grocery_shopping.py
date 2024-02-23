from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class GroceryShopping(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    budget = db.Column(db.Float, nullable=False)
    store_preference = db.Column(db.String(100), nullable=False)

    def __init__(self, budget, store_preference):
        self.budget = budget
        self.store_preference = store_preference
