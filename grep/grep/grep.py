import glob

files = glob.glob("*.txt") 

file_name = input("Enter file name: ")
pattern = input("Enter pattern: ")

for f in files:
    file = open(file_name, "r")
    lines = file.readline()
    for i, line in enumerate(lines):
        if pattern in lines:
            print(file_name, (i+1), lines.strip())
