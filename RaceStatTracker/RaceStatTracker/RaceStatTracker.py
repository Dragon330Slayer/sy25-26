import requests
from bs4 import BeautifulSoup

# Fetch the page
url = 'https://www.fiawec.com/en/page/manufacturers-classification/34'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

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

# Only show the first nine rows, which is eight manufacturers plus the header
print("Manufacturer Standings and Race Points:")
for position, manufacturer, race_points, total_points in standings[:8]:
    race_points_str = ', '.join(race_points)
    print(f"Position: {position}, Manufacturer: {manufacturer}, Race Points: [{race_points_str}], Total: {total_points}")