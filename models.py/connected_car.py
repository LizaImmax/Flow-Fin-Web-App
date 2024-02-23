from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ConnectedCar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    car_model = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    fuel_type = db.Column(db.String(50), nullable=False)
    
    # Additional fields
    mileage = db.Column(db.Float)
    color = db.Column(db.String(50))

    # You can add more fields as needed.

    def __init__(self, car_model, year, fuel_type, mileage=None, color=None):
        self.car_model = car_model
        self.year = year
        self.fuel_type = fuel_type
        self.mileage = mileage
        self.color = color
