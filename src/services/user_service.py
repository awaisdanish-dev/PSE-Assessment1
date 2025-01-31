import bcrypt
from src.database.db_connection import DatabaseConnection
from src.models.user import User

class UserService:
    def __init__(self):
        db_instance = DatabaseConnection()
        self.user_collection = db_instance.get_user_collection()

    def register_user(self, email, password, role="customer"):
        if self.user_collection.find_one({"email": email}):
            return False 

        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        new_user = User(email=email, password_hash=password_hash, role=role)
        self.user_collection.insert_one(new_user.to_dict())
        return True

    def validate_login(self, email, password):
        user_record = self.user_collection.find_one({"email": email})
        if user_record:
            if bcrypt.checkpw(password.encode('utf-8'), user_record["password_hash"]):
                return user_record
        return None
