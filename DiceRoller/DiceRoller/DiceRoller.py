import random

def show_dice(n):
    if n == 1:
        print("-----")
        print("|   |")
        print("| o |")
        print("|   |")
        print("-----")
    elif n == 2:
        print("-----")
        print("|o  |")
        print("|   |")
        print("|  o|")
        print("-----")
    elif n == 3:
        print("-----")
        print("|o  |")
        print("| o |")
        print("|  o|")
        print("-----")
    elif n == 4:
        print("-----")
        print("|o o|")
        print("|   |")
        print("|o o|")
        print("-----")
    elif n == 5:
        print("-----")
        print("|o o|")
        print("| o |")
        print("|o o|")
        print("-----")
    elif n == 6:
        print("-----")
        print("|o o|")
        print("|o o|")
        print("|o o|")
        print("-----")

guess = 0 
r = 1
count = 0

while guess != r:
    guess = int(input("Guess the dice roll (1-6): "))
    r = random.randint(1, 6)
    show_dice(r)
    count = count + 1

print(f"Correct! It took you {count} tries to guess the number {r}.")
  
