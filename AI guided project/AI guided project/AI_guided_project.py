race_name = input("Enter the race name: ")  
filename = race_name + ".txt"  

  
with open(filename, 'r') as file:  
    for line in file:  
        parts = line.strip().split('|')  
        placement = parts[0]  
        driver_number = parts[1]  
        points = parts[2]  
        name = parts[3]  
        team = parts[4]  
        print(f"{placement}: #{driver_number} {name} ({team}) - {points} points")  
