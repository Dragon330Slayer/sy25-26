inventory =  []
while True:
    print("\nOptions: [1] Add [2] Remove [3] List [4] Exit")
    choice = input("Select an option (1-4): ")
    if choice == 1:
        name = input("Enter item name: ").strip().capitalize()
        qty = int(input(f"How many {name}s"))
        inventory.append((name, qty))
    elif choice == 2:
        name = input("Which item would you like to remove: ").strip().capitalize()
        inventory = [item for item in inventory if item[0] != name]
    elif choice == 3:
        if not inventory:
            print("Inventory is empty.")
        else:
            print("Current Inventory:")
            for item in inventory:
                print(f"{item[0]}: {item[1]}")
    elif choice == 4:
        print("Exiting Inventory Manager. Goodbye!")
        break
    else:
        print("Invalid option. Please select a number between 1 and 4.")
