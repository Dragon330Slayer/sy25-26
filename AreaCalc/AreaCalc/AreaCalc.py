# This calculates the area of a circle
radius = float(input("Enter the radius of the circle: "))
area = 3.14159 * radius * radius
print(f"The area of the circle is: {area}")
print()
# This calculates the area of a rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
print(f"The area of the rectangle is: {area}")

# This calculates the area of a hexagon
side = float(input("Enter the side length of the hexagon: "))
area = (3 * (3**0.5) * side * side) / 2
print(f"The area of the hexagon is: {area}")
print()