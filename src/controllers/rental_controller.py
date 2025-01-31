from src.services.rental_service import RentalService
from colorama import Fore, Style, init

init(autoreset=True)

class RentalController:

    def __init__(self, user):
        self.rental_service = RentalService()
        self.user_email = user["email"]

    def view_available_cars(self):

        print(Fore.CYAN + "\n🚗 === Available Cars for Rent === 🚗")
        cars = self.rental_service.list_available_cars()

        if not cars:
            print(Fore.RED + "😢 No cars currently available.")
        else:
            print(Fore.YELLOW + "\n📋 Available Cars:")
            for c in cars:
                print(Fore.GREEN + f"🆔 CarID: {c['car_id']} | 🚘 {c['make']} {c['model']} | 📅 Year: {c['year']} | "
                      f"🛞 Mileage: {c['mileage']} | 💰 Daily Rate: ${c['daily_rate']}")

    def make_booking(self):

        print(Fore.CYAN + "\n📝 === Make a Booking === 📝")
        car_id = input(Fore.YELLOW + "🆔 Enter Car ID to book: ").strip()
        start_date = input(Fore.YELLOW + "📅 Enter Start Date (YYYY-MM-DD): ").strip()
        end_date = input(Fore.YELLOW + "📅 Enter End Date (YYYY-MM-DD): ").strip()

        success, msg = self.rental_service.book_car(self.user_email, car_id, start_date, end_date)
        if success:
            print(Fore.GREEN + f"✅ Booking confirmed for {car_id} from {start_date} to {end_date}.")
        else:
            print(Fore.RED + f"❌ {msg}")
