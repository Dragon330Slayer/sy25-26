filename = input("Enter the filename (Bee Movie.txt or Gettysburg Address.txt): ")
file = open(filename, "r")

word = input("Enter the word to search for: ")

line = file.readline()
while line:
    line = file.readline()

file.close()