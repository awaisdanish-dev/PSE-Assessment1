from pymongo import MongoClient
import ssl

class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            try:
                MONGODB_URI = "mongodb+srv://admin:admin@rentalsystem.zxner.mongodb.net/?retryWrites=true&w=majority&appName=rentalsystem"
                cls._instance.client = MongoClient(MONGODB_URI, tlsAllowInvalidCertificates=True)
                cls._instance.db = cls._instance.client["car_rental_db"]
            except Exception as e:
                print(f"[ERROR] Could not connect to MongoDB: {e}")
                exit(1)
        return cls._instance

    def get_user_collection(self):
        return self.db["users"]

    def get_car_collection(self):
        return self.db["cars"]

    def get_rental_collection(self):
        return self.db["rentals"]
