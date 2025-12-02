import random

turn = 1
score = 0
round = 0
roll = 0
answer = ""

print("turn", turn)
print("Your current score is", score)
print("This round you have", round)
answer = input("Would you like to roll or bank? ")

while True:
    if answer == "roll":
        roll = random.randint(1, 6)
        print("You rolled a", roll)
        if roll != 1:
            round_points += roll
        else:
            round_points = 0
            print("You get nothing for this round.")
            break
        print("This round you have", round_points)
        answer = input("Would you like to roll or bank? ")

    if answer == "bank":
        human_score += round_points
        round_points = 0
        print("You banked your points. Your total score is now", human_score)
        if human_score >= 100:
            print("Congratulations! You win with a score of", human_score)
            break

    print("\nTurn", turn, "- AI's turn")
    round_points = 0
    while True:
        roll = random.randint(1, 6)
        print("AI rolled a", roll)
        if roll == 1:
            round_points = 0
            print("AI gets nothing for this round.")
            break
        round_points += roll
        print("AI's round points are now", round_points)
        if roll <= 3:  
            ai_score += round_points
            print("AI banks its points. AI's total score is now", ai_score)
            break

    if ai_score >= 100:
        print("AI wins with a score of", ai_score)
        break

    turn += 1