gear_database = {
    "beginner": {
        "bat": ["Kookaburra", "SG basic", "SS Ton"],
        "gloves": ["GM Gloves", "SS Gloves"],
        "shoes": ["Puma", "Adidas"],
        "helmet": ["Shrey Basic", "SG"]
    },
    "intermediate": {
        "bat": ["MRF", "SG Scorer", "SS Master"],
        "gloves": ["SG Gloves", "MRF Gloves"],
        "shoes": ["Nike", "Adidas XT"],
        "helmet": ["Shrey Elite", "MRF"]
    },
    "professional": {
        "bat": ["MRF Chase Master", "SS Limited Edition"],
        "gloves": ["SS Test Gloves", "MRF Pro Gloves"],
        "shoes": ["Puma Pro"],
        "helmet": ["Shrey Masterclass"]
    }
}

print("Welcome to the Cricket Gear Recommendation System!")

while True:
    name = input("Enter Player Name: ")
    age = int(input("Enter Player Age: "))
    location = input("Enter City (e.g., Hyderabad, Delhi, Mumbai): ")
    
    if age <= 0:
        print("Invalid age! Please enter a valid age.")
        continue

    if age < 12:
        print("\nSpecial Kit for kids: Lightweight bat, soft gloves, rubber-spiked shoes, and a small-size helmet.")
        choice = input("\nDo you want to enter another player? (yes/no): ").lower()
        if choice != 'yes':
            print("\nThank you for using the Cricket Gear Recommendation System!")
            break
        continue

    l = input("Enter Skill Level (beginner/intermediate/professional): ").lower()

    if l not in gear_database:
        print("Invalid skill level! Please choose beginner, intermediate, or professional.")
        continue

    print("\nAvailable Gear Types: bat, gloves, shoes, helmet")
    preferences = input("Enter preferred gear types (comma-separated): ").split(',')

    print(f"\nHello {name} from {location}! Here's your recommended cricket gear:")

    for gear in preferences:
        gear = gear.strip().lower()
        if gear in gear_database[l]:
            print(f"\n{gear.capitalize()} Recommendations for {l.capitalize()} Level:")
            for item in gear_database[l][gear]:
                print(f" - {item}")
        else:
            print(f"\nSorry, we don't have recommendations for '{gear}'.")

    choice = input("\nDo you want to enter another player? (yes/no): ").lower()
    if choice != 'yes':
        print("\nThank you for using the Cricket Gear Recommendation System!")
        break
