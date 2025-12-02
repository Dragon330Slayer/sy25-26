import requests
from bs4 import BeautifulSoup

# URLs for Hypercar and LMGT3 manufacturer standings
hypercar_url = 'https://www.fiawec.com/en/page/manufacturers-classification/34'
lmgt3_url = 'https://www.fiawec.com/en/page/manufacturers-classification/34'  # Update if the actual LMGT3 URL is different

# List of race names in the order they appear in the table
race_names = [
    "Qatar", "Italy", "Belgium", "France", "Brazil", "United States", "Japan", "Bahrain"]

def fetch_standings(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    standings = []
    for row in soup.select('table tbody tr'):
        columns = row.find_all('td')
        if len(columns) > 3:
            position = columns[0].get_text(strip=True)
            manufacturer = columns[1].get_text(strip=True)
            race_points = [col.get_text(strip=True) for col in columns[2:-1]]
            total_points = columns[-1].get_text(strip=True)
            standings.append((position, manufacturer, race_points, total_points))
    return standings

# Ask the user which championship they want to see
championship_choice = input("Do you want to see Hypercar or LMGT3 standings? (Enter 'Hypercar' or 'LMGT3'): ").strip().lower()

if championship_choice == 'hypercar':
    standings = fetch_standings(hypercar_url)
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
        print("\nHypercar Manufacturer Championship Standings (Top 8):")
        for position, manufacturer, race_points, total_points in standings[:8]:
            print(f"Position: {position}, Manufacturer: {manufacturer}, Total Points: {total_points}")
    else:
        print("Invalid choice. Please enter 'race' or 'championship'.")
elif championship_choice == 'lmgt3':
    standings = fetch_standings(lmgt3_url)
    # Skip the first 41 rows and use the next 18 rows
    lmgt3_standings = standings[41:59]
    choice = input("Do you want to see a specific race or the manufacturer championship? (Enter 'race' or 'championship'): ").strip().lower()
    if choice == 'race':
        print("Available races:")
        for name in race_names:
            print(f"- {name}")
        race_choice = input("Enter the race name: ").strip().title()
        if race_choice in race_names:
            race_idx = race_names.index(race_choice)
            print(f"\nResults for {race_choice} (Top 18):")
            for position, manufacturer, race_points, total_points in lmgt3_standings:
                if race_idx < len(race_points):
                    print(f"Position: {position}, Manufacturer: {manufacturer}, Race Points: {race_points[race_idx]}")
                else:
                    print(f"Position: {position}, Manufacturer: {manufacturer}, Race Points: N/A")
        else:
            print("Invalid race name.")
    elif choice == 'championship':
        print("\nLMGT3 Manufacturer Championship Standings (Top 18):")
        for position, manufacturer, race_points, total_points in lmgt3_standings:
            print(f"Position: {position}, Manufacturer: {manufacturer}, Total Points: {total_points}")
    else:
        print("Invalid choice. Please enter 'race' or 'championship'.")
else:
    print("Invalid choice. Please enter 'Hypercar' or 'LMGT3'.")


            