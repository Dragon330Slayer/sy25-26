def placements():
    placements = []

    while True:
        entry = input("Enter a placement (or type 'done' to finish): ")
        if entry.lower() == 'done':
            break
            placements.append(entry)

    # Assign points: 1st = 25, 2nd = 18, 3rd = 15, 4th = 12, 5th = 10, 6th = 8, 7th = 6, 8th = 4, 9th = 2, 10th = 1 11+ = 0
    points = {}
    max_points = 25

    for idx, name in enumerate(placements):
        point = max(max_points - idx, 1)  # Ensure minimum 0 point
        points[name] = point

    print("Final placements and points:")
    for name, point in points.items():
        print(f"{name}: {point} points")



import requests
from bs4 import BeautifulSoup

# Fetch the page
url = 'https://www.fiawec.com/en/page/manufacturers-classification/34'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Inspect the page to find the correct selector for placements
placements = []
for row in soup.select('table tbody tr'):
    columns = row.find_all('td')
    if columns:
        # Adjust the index based on the actual table structure
        team_name = columns[5].get_text(strip=True)
        placements.append(team_name)

# Assign points: 1st = 25, 2nd = 18, 3rd = 15, 4th = 12, 5th = 10, 6th = 8, 7th = 6, 8th = 4, 9th = 2, 10th = 1, 11+ = 0
points_table = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]
points = {}

for idx, name in enumerate(placements):
    point = points_table[idx] if idx < len(points_table) else 0
    points[name] = point

print("Final placements and points:")
for name, point in points.items():
    print(f"{name}: {point} points")