import requests
from bs4 import BeautifulSoup

# Fetch the page
url = 'https://www.fiawec.com/en/page/manufacturers-classification/34'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# List of race names in the order they appear in the table
race_names = [
    "Qatar", "Italy", "Belgium", "France", "Brazil", "United States", "Japan", "Bahrain"
]

# Find the manufacturers standings table
standings = []
for row in soup.select('table tbody tr'):
    columns = row.find_all('td')
    if len(columns) > 3:  # Ensure there are enough columns
        position = columns[0].get_text(strip=True)
        manufacturer = columns[1].get_text(strip=True)
        # Extract points for each race (assuming columns 2 to -2 are race points, adjust as needed)
        race_points = [col.get_text(strip=True) for col in columns[2:-1]]
        total_points = columns[-1].get_text(strip=True)
        standings.append((position, manufacturer, race_points, total_points))

# Ask the user what they want to see
choice = input("Do you want to see a specific race or the manufacturer championship? (Enter 'race' or 'championship'): ").strip().lower()

if choice == 'race':
    print("Available races:")
    for name in race_names:
        print(f"- {name}")
    race_choice = input("Enter the race name: ").strip().title()
    if race_choice in race_names:
        race_idx = race_names.index(race_choice)
        print(f"\nResults for {race_choice} (Top 8):")
        for position, manufacturer, race_points, total_points in standings[:8]:
            if race_idx < len(race_points):
                print(f"Position: {position}, Manufacturer: {manufacturer}, Race Points: {race_points[race_idx]}")
            else:
                print(f"Position: {position}, Manufacturer: {manufacturer}, Race Points: N/A")
    else:
        print("Invalid race name.")
elif choice == 'championship':
    print("\nManufacturer Championship Standings (Top 8):")
    for position, manufacturer, race_points, total_points in standings[:8]:
        print(f"Position: {position}, Manufacturer: {manufacturer}, Total Points: {total_points}")
else:
    print("Invalid choice. Please enter 'race' or 'championship'.")
