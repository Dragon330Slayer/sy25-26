fname = "output.txt"
file = open(fname, "a")
for i in range(10):
    file.write(f"This is line {i}.\n")
file.close()
