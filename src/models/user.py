# src/models/user.py

class User:
    def __init__(self, email, password_hash, role="customer"):
        self.email = email
        self.password_hash = password_hash
        self.role = role

    def to_dict(self):
        return {
            "email": self.email,
            "password_hash": self.password_hash,
            "role": self.role
        }
