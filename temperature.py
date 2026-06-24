# Welcome message
print("Welcome to Simple Temperature Conversions!")

# Ask user to enter a temperature value
y=float(input("Enter the original temperature value (in numbers only) "))

# Show the option menu to the user (original temperature unit)
print("What temperature do you want convert from?")
print("1.Kelvin (K)")
print("2. Celsius (°C)")
print("3. Fahrenheit (°F)")
print("4. Reamur (°R)")
source = input("Enter your choice (1-4) ")

# Show the option menu to the user (target temperature unit)
# If source from 1. Kelvin
if source == "1":
    print("What temperature unit do you want to convert to?")
    print("1.Celsius (°C)")
    print("2. Fahrenheit (°F)")
    print("3. Reamur (°R)")
    target=input("Enter your choice (1-3) ")
    if target == "1":
        print(f"{round (y - 273.15, 2)} °C")
    elif target == "2":
        print(f"{round ((y - 273.15)* 9/5 + 32, 2)} °F")
    elif target == "3":
        print(f"{round(4/5 * (y - 273.15), 2)} °R")
    else:
        print("Invalid choice, please enter a number from 1-3")

# If source from 2. Celsius
elif source == "2":
    print("What temperature unit do you want to convert to?")
    print("1.Kelvin (K)")
    print("2. Fahrenheit (°F)")
    print("3. Reamur (°R)")
    target=input("Enter your choice (1-3) ")
    if target == "1":
        print(f"{round (y + 273.15, 2)} K")
    elif target == "2":
        print(f"{round((y * 9/5)+ 32)} °F")
    elif target == "3":
        print(f"{round(4/5 * y, 2) } °R")
    else:
        print("Invalid choice, please enter a number from 1-3")

# If source from 3. Fahrenheit
elif source == "3":
    print("What temperature unit do you want to convert to?")
    print("1.Kelvin (K)")
    print("2. Celsius (°C)")
    print("3. Reamur (°R)")
    target=input("Enter your choice (1-3) ")
    if target == "1":
        print(f"{round((y - 32)*5/9+273.15, 2)} K")
    elif target == "2":
        print(f"{round(5/9 * (y-32), 2)} °C")
    elif target == "3":
        print(f"{round(4/9 * (y-32), 2) } °R")
    else:
        print("Invalid choice, please enter a number from 1-3")

# If source from 4. Reamur
elif source == "4":
    print("What temperature unit do you want to convert to?")
    print("1.Kelvin (K)")
    print("2. Celsius (°C)")
    print("3. Fahrenheit (°F)")
    target=input("Enter your choice (1-3) ")
    if target == "1":
        print(f"{round ((5/4 * y) + 273.15, 2)} K")
    elif target == "2":
        print(f"{round(5/4 * y, 2 )} °C")
    elif target == "3":
        print(f"{round((9/4 * y) + 32, 2)} °F")
    else:
        print("Invalid choice, please enter a number from 1-3")

else:
        print("Invalid choice, please enter a number from 1-4")
        
# Closing
print("Your temperature has been converted. Thank you for using this Simple Temperature Conversion tool. We hope this was helpful!")

