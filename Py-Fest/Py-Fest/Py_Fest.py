# The initial lineup
lineup = [
    ("Code Play", "Indie", 30),
    ("The Pythonistas", "Rock", 45),
    ("Syntax Error", "Metal", 60)
]

while True:
    print("\n---Py-Fest 2026 Stage Manager---")
    print("1. View Lineup & Total Time")
    print("2. Add a New Band")
    print("3. Move First Band to End (Late Arrival)")
    print("4. Remove Band by Name")
    print("5. Move Band to SPecific Position")
    print("6. Exit")
    print(f"Total Festival Duration: {total_time} minutes")
    choice = input("Select an option (1-6): ")

    if choice == "1":
        print("\n---Current Lineup---")
        print(lineup)
        
    elif choice == "2":
        name = input("Enter band name: ")
        genre = input("Enter band genre: ")
        duration = int(input("Enter performance duration (in minutes): "))
        lineup.append((name, genre, duration))
        total_time += duration
        print(f"{name} added")
        print(f"{i}. {name} ({genre}) - {duration} mins")

