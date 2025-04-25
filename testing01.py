# Python program to test the functions by Tuomas Kivioja


def ask_name():
    name = input("What is your name? ").capitalize()
    return name


def calculate_expences(whatever):
    sum_total = sum(whatever)
    return sum_total


exp = [20.3, 50.3, 70.1, 86.3]

command = input("Which command do you want to test? (1. name or 2 expences): ")

if command == "1":
    print(ask_name())
    print(type)
elif command == "2":
    print("The sum of the expenses is:")
    print(calculate_expences(exp))
    print(type(calculate_expences(exp)))
else:
    print("Invalid command. Please enter 1 or 2.")

# The code above is a simple Python program that defines two functions: ask_name and calculate_expences.
