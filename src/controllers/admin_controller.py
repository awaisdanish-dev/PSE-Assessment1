import sys
from src.services.admin_service import AdminService
from src.services.rental_service import RentalService
from colorama import Fore, Style, init

init(autoreset=True)

class AdminController:

    def __init__(self):
        self.admin_service = AdminService()
        self.rental_service = RentalService()

    def manage_cars(self):
 
        while True:
            print(Fore.BLUE + "\n🚗 === Admin: Manage Cars === 🚗")
            print(Fore.YELLOW + "1️⃣  Add Car")
            print(Fore.CYAN + "2️⃣  Update Car")
            print(Fore.RED + "3️⃣  Delete Car")
            print(Fore.GREEN + "4️⃣  View Available Cars 🛞")
            print(Fore.MAGENTA + "5️⃣  Return to Admin Menu")

            choice = input(Fore.WHITE + "Enter choice: ").strip()

            if choice == "1":
                self.add_car_flow()
            elif choice == "2":
                self.update_car_flow()
            elif choice == "3":
                self.delete_car_flow()
            elif choice == "4":
                self.view_available_cars()
            elif choice == "5":
                print(Fore.YELLOW + "🔙 Returning to Admin Menu...")
                break
            else:
                print(Fore.RED + "❌ Invalid choice. Try again.")

    def add_car_flow(self):

        print(Fore.GREEN + "\n🚘 === Add Car === 🚘")
        car_id = input("🆔 Car ID: ").strip()
        make = input("🏎️ Make: ").strip()
        model = input("📌 Model: ").strip()
        year = input("📅 Year: ").strip()
        mileage = input("🛞 Mileage: ").strip()
        available_now = input("✅ Is car available now? (y/n): ").strip().lower() == "y"
        min_rent_period = int(input("📆 Min rent period (days): ").strip())
        max_rent_period = int(input("📆 Max rent period (days): ").strip())
        daily_rate = float(input("💰 Daily rate: ").strip())

        success, msg = self.admin_service.add_car(
            car_id, make, model, year, mileage, available_now,
            min_rent_period, max_rent_period, daily_rate
        )
        print(Fore.GREEN + msg if success else Fore.RED + msg)

    def view_available_cars(self):
 
        print(Fore.GREEN + "\n🚙 === Available Cars === 🚙")
        available_cars = self.admin_service.list_available_cars()

        if not available_cars:
            print(Fore.RED + "😢 No available cars at the moment.")
            return

        for car in available_cars:
            print(Fore.CYAN + f"🆔 CarID={car['car_id']} | 🚘 {car['make']} {car['model']} | 📅 Year={car['year']} | 🛞 Mileage={car['mileage']} | 💰 Daily Rate=${car['daily_rate']}")

    def update_car_flow(self):
 
        print(Fore.CYAN + "\n🛠️ === Update Car === 🛠️")
        self.view_available_cars()

        car_id = input(Fore.WHITE + "🆔 Enter Car ID to update: ").strip()
        field = input("🔧 Which field to update? (make, model, available, daily_rate): ").strip()
        new_value = input("✏️ New value: ").strip()

        if field == "available":
            new_value = (new_value.lower() == "true" or new_value.lower() == "y")
        elif field in ["daily_rate"]:
            new_value = float(new_value)
        elif field in ["min_rent_period", "max_rent_period"]:
            new_value = int(new_value)

        success, msg = self.admin_service.update_car(car_id, field, new_value)
        print(Fore.GREEN + msg if success else Fore.RED + msg)

    def delete_car_flow(self):

        print(Fore.RED + "\n🚗 🗑️  === Delete Car === 🗑️ 🚗")
        self.view_available_cars()

        car_id = input(Fore.WHITE + "\nEnter Car ID to delete: ").strip()
        success, msg = self.admin_service.delete_car(car_id)
        print(Fore.GREEN + f"✅ {msg}" if success else Fore.RED + f"❌ {msg}")

    def manage_bookings(self):

        while True:
            print(Fore.BLUE + "\n📆 === Admin: Manage Bookings === 📆")
            print(Fore.YELLOW + "1️⃣  List Pending Bookings")
            print(Fore.CYAN + "2️⃣  Approve a Booking ✅")
            print(Fore.RED + "3️⃣  Reject a Booking ❌")
            print(Fore.GREEN + "4️⃣  List All Bookings 📋")
            print(Fore.MAGENTA + "5️⃣  Return to Admin Menu")

            choice = input(Fore.WHITE + "Enter choice: ").strip()

            if choice == "1":
                rentals = self.rental_service.list_rentals(status="pending")
                if rentals:
                    for r in rentals:
                        print(Fore.CYAN + f"📌 ID={r['_id']} | 🚘 CarID={r['car_id']} | 📧 User={r['user_email']} | 🏷️ Status={r['status']} | 💰 Fee=${r['total_fee']}")
                else:
                    print(Fore.RED + "🚫 No pending rentals.")

            elif choice == "2":
                rental_id = input(Fore.WHITE + "🆔 Enter Rental ID to approve: ").strip()
                success, msg = self.rental_service.approve_rental(rental_id)
                print(Fore.GREEN + msg if success else Fore.RED + msg)

            elif choice == "3":
                rental_id = input(Fore.WHITE + "🆔 Enter Rental ID to reject: ").strip()
                success, msg = self.rental_service.reject_rental(rental_id)
                print(Fore.GREEN + msg if success else Fore.RED + msg)

            elif choice == "4":
                rentals = self.rental_service.list_rentals()
                for r in rentals:
                    print(Fore.CYAN + f"📌 ID={r['_id']} | 🚘 CarID={r['car_id']} | 📧 User={r['user_email']} | 🏷️ Status={r['status']} | 💰 Fee=${r['total_fee']}")

            elif choice == "5":
                print(Fore.YELLOW + "🔙 Returning to Admin Menu...")
                break

            else:
                print(Fore.RED + "❌ Invalid choice. Try again.")
