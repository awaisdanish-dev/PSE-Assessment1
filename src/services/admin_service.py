from src.database.db_connection import DatabaseConnection
from src.models.car import Car

class AdminService:

    def __init__(self):
        db_instance = DatabaseConnection()
        self.car_collection = db_instance.get_car_collection()
    
    def list_available_cars(self):
        return list(self.car_collection.find({"available": True}, {"_id": 0})) 


    def add_car(self, car_id, make, model, year, mileage, available, min_rent_period, max_rent_period, daily_rate):
        existing = self.car_collection.find_one({"car_id": car_id})
        if existing:
            return False, "Car with this ID already exists."

        new_car = Car(
            car_id=car_id,
            make=make,
            model=model,
            year=year,
            mileage=mileage,
            available=available,
            min_rent_period=min_rent_period,
            max_rent_period=max_rent_period,
            daily_rate=daily_rate
        )
        self.car_collection.insert_one(new_car.to_dict())
        return True, "Car added successfully."

    def update_car(self, car_id, field, new_value):
        result = self.car_collection.update_one({"car_id": car_id}, {"$set": {field: new_value}})
        if result.modified_count > 0:
            return True, f"{field} updated successfully."
        else:
            return False, "Update failed. Car not found or same value."

    def delete_car(self, car_id):
        result = self.car_collection.delete_one({"car_id": car_id})
        if result.deleted_count > 0:
            return True, "Car deleted successfully."
        else:
            return False, "Car not found."
