class Rental:

    def __init__(self, car_id, user_email, start_date, end_date, status="pending", total_fee=0):
        self.car_id = car_id
        self.user_email = user_email
        self.start_date = start_date
        self.end_date = end_date
        self.status = status    
        self.total_fee = total_fee

    def to_dict(self):
        return {
            "car_id": self.car_id,
            "user_email": self.user_email,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "status": self.status,
            "total_fee": self.total_fee
        }
