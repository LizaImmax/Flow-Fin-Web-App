from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class HealthTracker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.Float, nullable=False)
    height = db.Column(db.Float, nullable=False)
    blood_pressure = db.Column(db.String(20), nullable=False)

    def __init__(self, weight, height, blood_pressure):
        self.weight = weight
        self.height = height
        self.blood_pressure = blood_pressure
