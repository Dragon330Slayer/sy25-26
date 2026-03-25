weight = float(input("Enter the weight of the potato in grams: "))
if weight < 100:
    grade = "small"
elif 100 <= weight < 200:
    grade = "medium"
else:
    grade = "large"
print(f"The potato is classified as: {grade}")

blemish_counts = []
for i in range(5):
    blemish_count = int(input(f"Enter the number of blemishes for potato {i + 1}: "))
    blemish_counts.append(blemish_count)
total = sum(blemish_counts)
average = total / len(blemish_counts)
print(f"total blemishes: {total}")
print(f"average blemishes: {average}")

all_potatoes = [0, 2, 5, 1, 0, 8, 3, 0]
perfect_potatoes = []
for p in all_potatoes:
    if p == 0:
        perfect_potatoes.append(p)
num_perfect = len(perfect_potatoes)
num_total = len(all_potatoes)
percentage = (num_perfect / num_total) * 100
print("perfect potatoes found: {num_perfect}")
print("percentage of perfect potatoes: {percentage}%")