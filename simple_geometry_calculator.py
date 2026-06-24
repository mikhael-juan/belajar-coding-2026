# import 'math' module, so that it can be used below
import math

# import 'sys' module, so that it can be used below if side/radius input <0
import sys

# Welcome message
print("Welcome to Simple Geometry Calculator!")
print("Before continuing, make sure that every input you give to this program is a number")
# Select options
print("1. Square")
print("2. Rectangle")
print("3. Right Triangle")
print("4. Circle")
shape=input("Select options 1-4 ")

# If Square
if shape=="1":
    s=float(input("Enter side: "))
    if s <= 0:
        print("Side must be greater than zero.")
        sys.exit()
    print(f"Area: {round(s**2, 2)}")
    print(f"Perimeter: {round(s*4, 2)}")
    print(f"Diagonal: {round (s* math.sqrt(2), 2)}")

# If Rectangle
elif shape=="2":
    l=float(input("Enter length "))
    if l <= 0:
        print("Lenght must be greater than zero.")
        sys.exit()
    w=float(input("Enter width "))
    if w <= 0:
        print("Width must be greater than zero.")
        sys.exit()
    print(f"Area: {round(l*w, 2)}")
    print(f"Perimeter: {round(2*(l+w), 2)}")
    print(f"Diagonal: {round(math.sqrt(l**2 + w**2), 2)}")

# If Right Triangle
elif shape=="3":
    a=float(input("Enter Side a (vertical side) "))
    if a <= 0:
        print("Vertical side must be greater than zero.")
        sys.exit()
    b=float(input("Enter Side b (base side) "))
    if b <= 0:
        print("Base side must be greater than zero.")
        sys.exit()

# Calculate hypotenuse automatically
    c=math.sqrt(a**2 + b**2)
    print(f"Hypotenuse: {round(c, 2)}")
    print(f"Area: {round(0.5*a*b, 2)}")
    print(f"Perimeter: {round(a+b+c, 2)}")

# If Circle
elif shape=="4":
    r=float(input("Enter radius "))
    if r <= 0:
        print("Radius must be greater than zero.")
        sys.exit()
    print(f"Area: {round(math.pi*r**2, 2)}")
    print(f"Perimeter: {round(2*math.pi*r, 2)}")

else:
    print("Invalid choice, please enter a number from 1-4")

# Closing
print("Calculation complete. Thank you for using Simple Geometry Calculator. We hope the results were useful!")