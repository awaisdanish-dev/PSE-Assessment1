class Car:
    def __init__(self, car_id, make, model, year, mileage, available, min_rent_period, max_rent_period, daily_rate):
        self.car_id = car_id
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.available = available
        self.min_rent_period = min_rent_period
        self.max_rent_period = max_rent_period
        self.daily_rate = daily_rate

    def to_dict(self):
        return {
            "car_id": self.car_id,
            "make": self.make,
            "model": self.model,
            "year": self.year,
            "mileage": self.mileage,
            "available": self.available,
            "min_rent_period": self.min_rent_period,
            "max_rent_period": self.max_rent_period,
            "daily_rate": self.daily_rate
        }
