from src.services.user_service import UserService
from colorama import Fore, Style, init

init(autoreset=True)

class UserController:

    def __init__(self):
        self.user_service = UserService()

    def register(self):

        print(Fore.CYAN + "\n📝 === User Registration === 📝")
        email = input(Fore.YELLOW + "📧 Enter email: ").strip()
        password = input(Fore.YELLOW + "🔑 Enter password: ").strip()

        print(Fore.CYAN + "\n👥 Choose role:")
        print(Fore.GREEN + "1️⃣  Customer (default)")
        print(Fore.MAGENTA + "2️⃣  Admin")

        role_choice = input(Fore.WHITE + "Enter choice [1/2]: ").strip()
        role = "admin" if role_choice == "2" else "customer"

        success = self.user_service.register_user(email, password, role)
        if success:
            print(Fore.GREEN + f"✅ Registration successful! Welcome, {email} as {role.upper()}.")
        else:
            print(Fore.RED + "❌ Registration failed. User may already exist.")

    def login(self):

        print(Fore.CYAN + "\n🔑 === User Login === 🔑")
        email = input(Fore.YELLOW + "📧 Enter email: ").strip()
        password = input(Fore.YELLOW + "🔒 Enter password: ").strip()

        user_record = self.user_service.validate_login(email, password)
        if user_record:
            print(Fore.GREEN + f"✅ Login successful! Welcome, {user_record['email']} (Role: {user_record['role'].upper()})")
            return user_record
        else:
            print(Fore.RED + "❌ Invalid credentials. Please try again.")
            return None
