from random import choice


A1 = ["A1", "Hundai Accent WRC", 220, (221,300), 5500, 5.4, 1998, 4]
A2 = ["A2", "Ford Focus WRC", 224, (221,300), 5400, 5.5, 1995, 4]
F2 = ["F2", "Mitsubishi Galant", 180, (216,300), 5800, 6.3, 3395, 4]
H2 = ["H2", "Mitsubishi Lancer", 198, (213,290), 5500, 7.2, 1997, 4]
G4 = ["G4", "Fiat Punto Kit-Car", 165, (161,220), 7500, 9.8, 1600, 4]
G1 = ["G1", "Citroen Visa 4x4", 190, (74,100), 7680, 9, 1566, 4]
C4 = ["C4", "Citroen Saxo Kit-Car", 168, (161,220), 7000, 7.5, 1600, 4]
G3 = ["G3", "Mitsubishi Pajero", 185, (153,208), 7000, 9.6, 3497, 6]
E4 = ["E4", "Austin Metro 6", 240, (265,360), 9800, 3.4, 3600, 6]
D1 = ["D1", "Mitsubishi Lancer RS", 220, (219,300), 6200, 5.9, 1997, 4]

cars = [A1, A2, F2, H2, G4, G1, C4, G3, E4, D1]

def print_car(c):
    print("_____________________________________________________")
    print(f"Code: {c[0]}" , "              |" , f"Model: {c[1]}")
    print(f"Top Speed: {c[2]} HP" , "     |" , f"0-100 km/h: {c[5]} seconds")
    print(f"Horsepower: {c[3][0]}-{c[3][1]} HP" , "|" , f"Engine Capacity: {c[6]} cc")
    print(f"RPM: {c[4]} RPM" , "         |" , f"Cylinders: {c[7]}")
    print("|______________________|_____________________________")

i = 1
for c in cars:
    print(i, c[1])
    i = i + 1
    print("")
choice = int(input("Select a car by entering the corresponding number: "))
print_car(cars[choice - 1])