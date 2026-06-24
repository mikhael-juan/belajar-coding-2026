# Welcome to Simple Calculator
print("Welcome to Simple Calculator!")

# Ask users for their name
name = input("Enter your name to get started ").strip().title()

# Say hello to users
print(f"Hello {name}! Feel free to start your calculation!")

x=float(input("Enter the first number "))
y=float(input("Enter the second number "))

# Show the options menu to the user
print("Select calculation operation")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
choice = input("Enter your choice (1-4) ")

# Run the matching calculation operation
if choice == "1":
    print(f"{x}+{y} = {x + y}")
elif choice == "2":
    print(f"{x}-{y} = {x - y}")
elif choice == "3":
    print(f"{x} * {y} = {x * y}")
elif choice == "4":
    if y == 0:
        print("Cannot divide by zero!")
    else:
        print(f"{x} / {y} = {round(x/y, 2)}")
    
else:
    print("Invalid choice, please enter a number from 1-4")

# Closing
print(f"Your calculation is done, {name}. Thanks for using Simple Calculator. Have a great day, {name}!")