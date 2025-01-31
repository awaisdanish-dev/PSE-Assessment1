from datetime import datetime
from src.database.db_connection import DatabaseConnection
from src.models.rental import Rental

class RentalService:

    def __init__(self):
        db_instance = DatabaseConnection()
        self.car_collection = db_instance.get_car_collection()
        self.rental_collection = db_instance.get_rental_collection()

    def list_available_cars(self):

        available_cars = self.car_collection.find({"available": True})
        return list(available_cars)

    def book_car(self, user_email, car_id, start_date_str, end_date_str):

        try:
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
        except ValueError:
            return False, "Invalid date format. Use YYYY-MM-DD."

        if end_date < start_date:
            return False, "End date cannot be before start date."

        car = self.car_collection.find_one({"car_id": car_id})
        if not car:
            return False, "Car does not exist."
        if not car["available"]:
            return False, "Car is not available."

        rental_days = (end_date - start_date).days + 1
        if rental_days < car["min_rent_period"] or rental_days > car["max_rent_period"]:
            return False, f"Rental period must be between {car['min_rent_period']} and {car['max_rent_period']} days."

        total_fee = car["daily_rate"] * rental_days

        new_rental = Rental(
            car_id=car_id,
            user_email=user_email,
            start_date=start_date_str,
            end_date=end_date_str,
            status="pending",
            total_fee=total_fee
        )
        self.rental_collection.insert_one(new_rental.to_dict())

        return True, f"Booking created successfully. Your total fee is ${total_fee}. Waiting for admin approval."

    def list_rentals(self, status=None):
 
        query = {}
        if status:
            query["status"] = status
        return list(self.rental_collection.find(query))

    def approve_rental(self, rental_id):

        from bson.objectid import ObjectId
        try:
            oid = ObjectId(rental_id)
        except:
            return False, "Invalid rental ID."

        rental = self.rental_collection.find_one({"_id": oid})
        if not rental:
            return False, "Rental not found."

        if rental["status"] != "pending":
            return False, "Cannot approve a rental that's not pending."

        self.rental_collection.update_one(
            {"_id": oid},
            {"$set": {"status": "approved"}}
        )
        self.car_collection.update_one(
            {"car_id": rental["car_id"]},
            {"$set": {"available": False}}
        )
        return True, "Rental approved successfully."

    def reject_rental(self, rental_id):
 
        from bson.objectid import ObjectId
        try:
            oid = ObjectId(rental_id)
        except:
            return False, "Invalid rental ID."

        rental = self.rental_collection.find_one({"_id": oid})
        if not rental:
            return False, "Rental not found."

        if rental["status"] != "pending":
            return False, "Cannot reject a rental that's not pending."

        self.rental_collection.update_one(
            {"_id": oid},
            {"$set": {"status": "rejected"}}
        )
        return True, "Rental rejected successfully."
