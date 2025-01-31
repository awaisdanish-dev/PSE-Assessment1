# 🚗 Car Rental System - README

## 📖 **Introduction**
The Car Rental CLI System is designed for both **customers and administrators** to efficiently manage car rentals via a **command-line interface (CLI)**. It provides functionalities such as **car browsing, booking, user authentication**, and **admin management of cars and bookings**.

---

## 🚀 **Step-by-Step Installation & Configuration**

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/awaisdanish-dev/PSE-Assessment1
cd car-rental-cli
```

### 2️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 3️⃣ **Run the Application**
```bash
python3 main.py
```

---

## 📂 **Project Structure & File Descriptions**

```
car-rental-cli/
│── src/
│   ├── controllers/          # Handles user/admin interactions
│   ├── services/             # Business logic for rentals, cars, users
│   ├── models/               # Data models for cars, users, rentals
│   ├── database/             # MongoDB connection setup
│   ├── utils/                # Helper functions (e.g., validation, formatting)
│── main.py                   # Entry point of the CLI application
│── requirements.txt           # List of required dependencies
│── README.md                  # Documentation file
```

### 📜 **File Explanations**
- `main.py`: The main entry point for starting the CLI application.
- `controllers/`: Handles the interactions between users/admins and the system.
- `services/`: Contains core business logic for handling car bookings, user management, etc.
- `models/`: Defines data models (Car, User, Rental).
- `database/`: Manages the MongoDB connection.
- `utils/`: Contains utility/helper functions.
- `requirements.txt`: Lists all dependencies needed to run the application.

---

## 📜 **License**
This project is licensed under the **MIT License**, meaning it can be freely used, modified, and distributed.

```
MIT License

Copyright (c) 2024 Muhammad Awais Danish

Permission is hereby granted, free of charge, to any person obtaining a copy...
```

---

## 🛠 **Known Bugs & Issues**
| Issue | Status |
|--------|------------|
| MongoDB connection errors | Ensure IP is whitelisted & correct credentials are used |
| Login fails for new users | Verify email & password format correctness |

If you encounter any bugs, please open an issue on GitHub.

---

## 👨‍💻 **Developer Credits**
**Developed by:** Muhammad Awais Danish  
**Email:** awaisdanish66@gmail.coml 
**GitHub:** [awaisdanish-dev](https://github.com/awaisdanish-dev)

---

