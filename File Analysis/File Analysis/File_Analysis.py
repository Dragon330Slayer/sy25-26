import glob

files = glob.glob("server_dump/*.txt")

status_counts = {"OK": 0, "WARN": 0, "ERROR": 0}
status_files = {"OK": [], "WARN": [], "ERROR": []}

for file in files:
    f = open(file, "r")
    content = f.read()
    for status in status_counts:
        if status in content:
            status_counts[status] += 1
            status_files[status].append(file)
            break

print("Status counts:")
for status, count in status_counts.items():
    print(f"{status}: {count}")


while True:
    print("\nChoose an option:")
    print("1. View files with status OK")
    print("2. View files with status WARN")
    print("3. View files with status ERROR")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ").strip()
    
    if choice == "1":
        print("\nFiles with status OK:")
        for filename in status_files["OK"]:
            print(f"  {filename}")
    elif choice == "2":
        print("\nFiles with status WARN:")
        for filename in status_files["WARN"]:
            print(f"  {filename}")
    elif choice == "3":
        print("\nFiles with status ERROR:")
        for filename in status_files["ERROR"]:
            print(f"  {filename}")
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
