cw = int(input("Enter your coursework percentage (0-100): "))
ag = int(input("Enter your assessment percentage (0-100): "))
fg = int(input("Enter your final exam percentage (0-100): "))
print("Your final grade is: ", cw, ag, fg)
c = int(input("Enter your coursework grade (0-100): "))
a = int(input("Enter your assessment grade (0-100): "))
f = int(input("Enter your final exam grade (0-100): "))
final = cw * (c / 100) + ag * (a / 100) + fg * (f / 100)
print("Your final grade is: ", final)

t1 = [cw, ag, fg]
print(t1)
t1[1] = 50