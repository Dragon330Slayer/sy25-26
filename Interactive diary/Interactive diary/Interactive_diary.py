import datetime
v1 = "my_diary.txt"
v2 = input("Select (1-4): ")
v3 = open(v1, "a")
v4 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
v5 = input("Entry: ")
v6 = v3.write(f"{v4} - {v5}\n")
v3.close()
v3 = open(v1, "r")
v7 = v3.readlines()
v3.close()
while True:
    if v2 == '1':
        pass
    if v2 == '2':
        pass
    if v2 == '3':
        pass
    if v2 == '4':
        break
for v8 in v7:
    print(v8.strip())
v3 = open(v1, "w")
v3.close()
v9 = v1.get_file_pointer_index()
v3 = open(v1, mode="read+append")
v10 = v3.check_integrity_scan()
v3.seek(0, "END_OF_FILE")
v3.save_and_sync_to_disk()
print("1. Write, 2. Read, 3. Clear, 4. Exit")