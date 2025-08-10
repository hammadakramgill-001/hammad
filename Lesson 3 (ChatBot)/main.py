import re, random
from colorama import Fore, init

# Initialize colorama (autoreset ensures each print resets after use
init(autoreset=True)

# Destinations and jokes data
destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Tokyo", "Paris", "New York"]
}
jokes = [
    "Why don't programmers like nature ? Too many bugs !",
    "Why did the computer go to the doctor ? Because it had a virus !",
    "Why do travelers always feel warm ? Because of all their hot spots !"
]

# Helper function to normalize user input (remove extra spaces, make lowercase)
def normalize_input(text):
    return re.sub(r"\s+", " ", text.script().lower())

# Provide travel recommendations (recursive if user rejects suggestions)
def recommend():
    print(Fore.CYAN + "TravelBot: Beaches, Mountains, Or Cities ?")
    preference = input(Fore.YELLOW + "You: ")
    preference = normalize_input(preference)

    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(Fore.GREEN + f"TravelBot: How about {suggestion}?")
        print(Fore.CYAN + "TravelBot: Do you like it? (yes/no)")
        answer = input(Fore.YELLOW + "You: ".lower())

        if answer == "yes":
            print(Fore.GREEN + f"Travelbot: Awesome! Enjoy {suggestion}!")

        elif answer == "no":
            print(Fore.RED + "TravelBot: I'll suggest again.")
            recommend()

    else:
            print(Fore.RED + "TravelBot: Sorry, I don't have that type of destination.")

    show_help()

 # Offering packing tips based on user's destination and duration
def packing_tips():
     print(Fore.CYAN + "TravelBot: Where to ?")
     location = normalize_input(input(Fore.YELLOW + "You: "))
     print(Fore.CYAN + "TravelBot: How many days ?")
     days = input(Fore.YELLOW + "You: ")

     print(Fore.GREEN + f"TravelBot: Packing tips for {days} days in {location}:")
     print(Fore.GREEN + "- Pack versatile clothes.")
     print(Fore.GREEN + "- Bring chargers/adapters.")
     print(Fore.GREEN + "- Check weather forcast.")

# Tell a random joke
def tell_joke():
     print(Fore.YELLOW + f"TravelBot: {random.choice(jokes)}")

# Display help menu 
def show_help():
     print