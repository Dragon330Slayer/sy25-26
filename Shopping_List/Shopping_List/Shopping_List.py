def print_menu():
    print("1. Add item")
    print("2. remove item")
    print("3. View list")
    print("4. Exit")
    return input("Please select an option: ")

def add_item():
    item = input("Enter the item to add: ")
    my_list.append(item)
    print(f"{item} has been added to your shopping list.")

def view_list():
    if not my_list:
        print("Your shopping list is empty.")
    else:
        print("Your shopping list contains:")
        for item in my_list:
            print(f"- {item}")

def remove_item():
    item = input("Enter the item to remove: ")
    if item in my_list:
        my_list.remove(item)
        print(f"{item} has been removed from your shopping list.")
    else:
        print(f"{item} is not in your shopping list.")

def new_item():
    item = input("Enter the new item: ")
    return item



choice = '0'
my_list = []
print("Welcome to your shopping list maager!")
while print_menu() != '4':
    choice = print_menu()
    print("You choice was: ", choice)
    if choice =="1":
        add_item()
    if choice == "3":
        view_list()