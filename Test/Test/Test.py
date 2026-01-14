# Py-Fest 2026 Stage Manager

def print_lineup(lineup):
    print("\n--- Current Lineup ---")
    total_time = 0
    for i, (name, genre, duration) in enumerate(lineup, 1):
        print(f"{i}. {name} ({genre}) - {duration} mins")
        total_time += duration
    print(f"\nTotal Festival Duration: {total_time} minutes")

def main():
    lineup = [
        ("Syntax Error", "Metal", 60)
    ]

    while True:
        print("\n---Py-Fest 2026 Stage Manager---")
        print("1. View Lineup & Total Time")
        print("2. Add a New Band")
        print("3. Move First Band to End (Late Arrival)")
        print("4. Remove a Band by Name")
        print("5. Move Band to Specific Position")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print_lineup(lineup)

        elif choice == "2":
            name = input("Enter band name: ")
            genre = input("Enter genre: ")
            try:
                duration = int(input("Enter performance duration (minutes): "))
                lineup.append((name, genre, duration))
                print(f"{name} added!")
            except ValueError:
                print("Invalid duration.")

        elif choice == "3":
            if len(lineup) > 1:
                late_band = lineup.pop(0)
                lineup.append(late_band)
                print(f"{late_band[0]} moved to end of lineup.")
            else:
                print("Not enough bands to swap!")

        elif choice == "4":
            name_to_remove = input("Enter the name of the band to remove: ")
            found = False
            for artist in lineup:
                if artist[0].lower() == name_to_remove.lower():
                    lineup.remove(artist)
                    print(f"{artist[0]} removed.")
                    found = True
                    break
            if not found:
                print(f"Band '{name_to_remove}' not found.")

        elif choice == "5":
            name_to_move = input("Enter the name of the band to move: ")
            found = False
            for idx, artist in enumerate(lineup):
                if artist[0].lower() == name_to_move.lower():
                    found = True
                    try:
                        new_pos = int(input(f"Enter new position (1-{len(lineup)}): "))
                        if 1 <= new_pos <= len(lineup):
                            band = lineup.pop(idx)
                            lineup.insert(new_pos - 1, band)
                            print(f"{band[0]} moved to position {new_pos}.")
                        else:
                            print("Please enter a valid number for the position.")
                    except ValueError:
                        print("Please enter a valid number for the position.")
                    break
            if not found:
                print(f"Band '{name_to_move}' not found.")

        elif choice == "6":
            print("Exiting Py-Fest Stage Manager.")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
