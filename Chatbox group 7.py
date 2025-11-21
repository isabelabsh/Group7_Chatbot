# Chatbot project - Group 7
# Members: Isabel, Nishita, Moraima
# Isabel added Japan, Italy, and Mexico.
# Nishita added India, France, and United Kingdom.
# Moraima added Canada, Venezuela, and Hungary
# This is a simple chatbot that responds with tourism info.

print("Chatbot project - Group 7")
print("Members: Isabel, Nishita, Moraima")


# Greeting
print("Welcome to the tourism chatbot.")
name = input("What is your name? ")
print(f"Nice to meet you, {name}! I can guide you through all of the stuff you want to know")
print("You can ask me about Japan, Italy, Mexico, India, France, United Kingdom, Canada, Venezuela or Hungary.")
print("Type 'bye' to end the chat.\n")


# Bonus: user trip expectation
trip_expectation = input("Before we start, what do you expect from your trip?")
print(f"Great! I will keep that in mind while helping you plan for your trip, {name}\n")

# Personalized suggestions
print("\nPersonalized Tips based on your Trip expectation:")

expectation = trip_expectation.lower()
matched_any = False

if "relax" in expectation or "peace" in expectation or "chill" in expectation:
    print("- You seem to want a relaxing trip! I'll recommend peaceful places.")
    matched_any = True
    
if "adventure" in expectation or "hiking" in expectation or "explore" in expectation:
    print("- You are an adventure lover! I'll keep that in mind.")
    matched_any = True
    
if "food" in expectation or "eat" in expectation or "cuisine" in expectation:
    print("- You love food! I'll share the best food spots in each country.")
    matched_any = True
    
if "shop" in expectation or "shopping" in expectation:
    print("- You enjoy shopping! I can suggest great shopping locations.")
    matched_any = True
    
if "history" in expectation or "culture" in expectation or "learn" in expectation:
    print("- You like history and culture! I'll include some educational places.")
    matched_any = True

# If nothing matches
if not matched_any:
    print("- Sounds like you're open to anything! I'll give a variety of suggestions.")
    
# Dictionary holding info for each country
tourism_data = {
    "japan": {
        "capital": "Tokyo",
        "food": ["sushi", "ramen"],
        "culture": "Modern cities mixed with old traditions.",
        "places": ["Tokyo Tower", "Mount Fuji"],
        "states": ["Osaka", "Kyoto"]
    },
    "italy": {
        "capital": "Rome",
        "food": ["pizza", "pasta"],
        "culture": "Known for art and old buildings.",
        "places": ["Colosseum", "Trevi Fountain"],
        "states": ["Tuscany", "Sicily"]
    },
    "mexico": {
        "capital": "Mexico City",
        "food": ["tacos", "tamales"],
        "culture": "Colorful celebrations and music.",
        "places": ["Zócalo", "Teotihuacán"],
        "states": ["Jalisco", "Yucatán"]
    },
    "india": {
        "capital": "New Delhi",
        "food": ["biryani", "dosa"],
        "culture": "Many festivals and languages.",
        "places": ["Taj Mahal", "Red Fort"],
        "states": ["Punjab", "Kerala"]
    },
    "france": {
        "capital": "Paris",
        "food": ["croissants", "baguettes"],
        "culture": "Art, cafes, and fashion.",
        "places": ["Eiffel Tower", "Louvre"],
        "states": ["Provence", "Normandy"]
    },
    "united kingdom": {
        "capital": "London",
        "food": ["fish and chips", "shepherd's pie"],
        "culture": "Tea, pubs, and old castles.",
        "places": ["Big Ben", "Tower Bridge"],
        "states": ["England", "Scotland"]
    },
    "canada":{
        "capital": "Ottawa",
        "food":["Maple Syrup Products", "Poutine", "Bannock"],
        "culture": "Canadians has a culture blend of indigenous and multicultural influences and more.",
        "places": ["Niagara Falls", "CN Tower", "Bay of Fundy"],
        "states": ["Toronto", "Montreal", "Quebec"]
    },
    "hungary":{
        "capital": "Budapest",
        "food":["Papri Kash", "Goulash", "Langos"],
        "culture": "Distinctive Cuisine, folk traditions, poetry, and more.",
        "places": ["Parliament Building", "Thermal Baths", "Danube River"],
        "states": ["Budapest", "Pecs", "Gyor"]
    },
    "venezuela":{
        "capital": "Caracas",
        "food":["Pabellon Criollo", "Arepas", "Cachapas"],
        "culture": "Venezuela is known for its music, festivals, and traditional foods.",
        "places": ["Angel Falls", "Los Roques Islands National Park", "Highest cable card in the world"],
        "states": ["Zulia", "Miranda", "Bolivar"]
    }
}

# Main Chatbot Loop 
while True:
    user_input = input("\nWhich place do you want to know about? ").lower()
    # Exit Condition
    if user_input == "bye":
        print("Goodbye! Have a great trip!")
        break
    
    # If we have data on the place   
    if user_input in tourism_data:
        info = tourism_data[user_input]
        print("\nTourism Information for", user_input.capitalize())
        print("Capital:", tourism_data[user_input]["capital"])
        
        print("Famous Foods:")
        for food in tourism_data[user_input]["food"]:
            print("-", food)
    
        print("Culture:")
        print("-", tourism_data[user_input]["culture"])
    
        print("Famous places to visit:")
        for place in tourism_data[user_input]["places"]:
            print("-", place)
        
        print("Famous States/Regions:")
        for state in tourism_data[user_input]["states"]:
            print("-", state)
        
        print("\nTrip Expectation Note:", trip_expectation)
        
        print("Any other place you want to know about?")

    # If the place is not recognized
    else:
        print("Sorry, I do not have information about that place.")
        print("Try Japan, Italy, Mexico, India, France, United Kingdom, Canada, Venezuela, or Hungary.")