from src.controllers.user_controller import UserController
from src.controllers.admin_controller import AdminController
from src.controllers.rental_controller import RentalController
from colorama import Fore, Style, init

init(autoreset=True)

def main():
    user_controller = UserController()
    admin_controller = None
    current_user = None

    while True:
        print(Fore.BLUE + "\n=======================================")
        print(Fore.YELLOW + "       🚗  Car Rental CLI System  🚗       ")
        print(Fore.BLUE + "=======================================")
        
        if not current_user:
            print(Fore.CYAN + "1️⃣  Register")
            print(Fore.GREEN + "2️⃣  Login")
            print(Fore.RED + "3️⃣  Exit")

            choice = input(Fore.WHITE + "Enter your choice: ").strip()

            if choice == "1":
                user_controller.register()
            elif choice == "2":
                logged_in_user = user_controller.login()
                if logged_in_user:
                    current_user = logged_in_user
                    print(Fore.GREEN + f"\n✅ Successfully logged in as {current_user['role'].upper()}!")
                    if current_user["role"] == "admin":
                        admin_controller = AdminController()
            elif choice == "3":
                print(Fore.RED + "\n👋 Exiting program. See you next time!")
                break
            else:
                print(Fore.RED + "❌ Invalid choice, please try again.")

        else:
            if current_user["role"] == "admin":
                print(Fore.MAGENTA + "\n🎩 === Admin Menu === 🎩")
                print(Fore.YELLOW + "1️⃣  Manage Cars 🚗")
                print(Fore.CYAN + "2️⃣  Manage Bookings 📅")
                print(Fore.RED + "3️⃣  Logout 🚪")

                choice = input(Fore.WHITE + "Enter your choice: ").strip()

                if choice == "1":
                    admin_controller.manage_cars()
                elif choice == "2":
                    admin_controller.manage_bookings()
                elif choice == "3":
                    print(Fore.RED + "\n🔓 Logging out...")
                    current_user = None
                    admin_controller = None
                    print(Fore.GREEN + "✅ Successfully logged out.")
                else:
                    print(Fore.RED + "❌ Invalid choice, please try again.")

            else:
                print(Fore.BLUE + "\n👤 === Customer Menu === 👤")
                print(Fore.YELLOW + "1️⃣  View Available Cars 🚘")
                print(Fore.CYAN + "2️⃣  Make a Booking 📝")
                print(Fore.RED + "3️⃣  Logout 🚪")

                choice = input(Fore.WHITE + "Enter your choice: ").strip()
                rental_controller = RentalController(current_user)

                if choice == "1":
                    rental_controller.view_available_cars()
                elif choice == "2":
                    rental_controller.make_booking()
                elif choice == "3":
                    print(Fore.RED + "\n🔓 Logging out...")
                    current_user = None
                    print(Fore.GREEN + "✅ Successfully logged out.")
                else:
                    print(Fore.RED + "❌ Invalid choice, please try again.")

if __name__ == "__main__":
    main()
