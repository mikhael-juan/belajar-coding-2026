print("Welcome! \nIn this Python file, the programmer has created four programs, each with a different theme and purpose. \nWe hope you enjoy trying them out and find them useful!")


# Part 1 (Use of if, elif, and else)
print(f"\nWelcome to program 1! \nThis program helps determine whether or not the two numbers you enter are equal.")
x=int(input("What's x? "))
y=int(input("What's y? "))

if x==y:
    print("x is equal to y")
else:
    print("x is not equal to y")


# Part 2 (Use of if, elif, and else with and)
print(f"\nWelcome to program 2! \nThis program helps classify your scores into predefined categories.")
score=int(input("Input your score (0-100): "))
if score >=90:
    print("Grade: A")
elif score >=80:
    print("Grade: B")
elif score >=70:
    print("Grade: C")
elif score >=60:
    print("Grade: D")
else:
    print("Grade: E")


# Part 3 (Use modulo operator %)
print(f"\nWelcome to program 3! \nThis program helps determine whether the number you input is odd or even")
x=int(input("What's x? "))

if x%2==0:
    print("Even")
else:
    print("Odd")


# Part 4 (Use modulo operator % to define a function, along with boolean true/false values)
print(f"\nWelcome to program 4! \nThis program helps you determine whether a number is a multiple of 3")
def main():
    x=int(input("What's x? "))
    if is_multiple_of_3(x):
        print("The number you entered is a multiple of 3")
    else:
        print("The number you entered is not a multiple of 3")

def is_multiple_of_3(n):
    return True if n%3==0 else False
main()

# Part 5 (Use modulo operator % to define a function, along with boolean true/false values)
print(f"\nWelcome to program 5! \nThis program helps you determine your Hogwarts house based on the name you enter.")
name=input("What's your name? ")

match name:
    case "Harry"|"Hermione"|"Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")