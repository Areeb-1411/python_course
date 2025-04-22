gear_database = {
    "beginner": {
        "bat": ["Kookaburra Kahuna", "SG RSD Spark", "SS Ton"],
        "gloves": ["GM Entry Gloves", "SS Beginners Gloves"],
        "shoes": ["Puma 20.1", "Adidas Howzat"],
        "helmet": ["Shrey Basic", "SG Optipro"]
    },
    "intermediate": {
        "bat": ["MRF Genius", "SG Scorer", "SS Master"],
        "gloves": ["SG League Gloves", "MRF Club Gloves"],
        "shoes": ["Nike Alpha", "Adidas XT"],
        "helmet": ["Shrey Elite", "MRF Dominate"]
    },
    "professional": {
        "bat": ["Gray Nicolls GN Pro", "MRF Chase Master", "SS Limited Edition"],
        "gloves": ["SS Test Gloves", "MRF Pro Gloves"],
        "shoes": ["Asics Gel-Peake", "Puma 22.1 Pro"],
        "helmet": ["Shrey Masterclass", "Masuri Vision Series"]
    }
}
gear_aliases = {
    "bats": "bat",
    "glove": "gloves",
    "glovs": "gloves",
    "shoe": "shoes",
    "helmets": "helmet",
    "helmat": "helmet"
}

print(" Welcome to the Cricket Gear Recommendation System!")

while True:
    print("\n Enter Player Details")

    name = input("Player Name: ")
    age = int(input("Age: "))
    if age <= 0:
        print(" Invalid age. Please try again.")
        continue
    location = input("City (Hyderabad, Delhi, Mumbai): ").strip().title()

    level = input("Skill Level (beginner/intermediate/professional): ").lower().strip()

    if level not in gear_database:
        print(" Invalid skill level. Please choose beginner, intermediate, or professional.")
        continue

    print("\nAvailable Gear Types: bat, gloves, shoes, helmet")
    preferences = input("Enter your preferred gear types (comma-separated): ").lower().split(',')
    preferences = [gear_aliases.get(p.strip(), p.strip()) for p in preferences]

    print(f"\n Hello {name} from {location}! Here's your recommended cricket gear:")

    for gear_type in preferences:
        if gear_type in gear_database[level]:
            print(f"\n{gear_type.capitalize()} Recommendations for {level.title()} Level:")
            for item in gear_database[level][gear_type]:
                print(f" - {item}")
        else:
            print(f"\n Sorry, we don't have recommendations for '{gear_type}'.")

    if age < 12:
        print("\n Special Junior Kit: Lightweight bat, soft gloves, rubber-spiked shoes, and a small-size helmet.")

    choice = input("\nDo you want to enter another user? (yes/no): ").lower()
    if choice != 'yes':
        print("\n Thank you for using the Cricket Gear Recommendation System! Stay sharp on the field.")
        break