#!/bin/python3

import time

# Coffee menu as a list
menu = ["Black coffee", "Cappuccino", "Latte", "Espresso"]

print("Hello stranger\nWelcome to our Coffee shop!\n")

# Get the user's name and capitalize it
name = input("What is your name? ").capitalize()

print(f"\nHello {name}, nice to see you here!")

time.sleep(1)

# Display the menu and take the user's order
print(f"\nHey {name}, what would you like? Here is our menu: {', '.join(menu)}.\n")

order = input().capitalize()

# Keep asking until the user provides a valid menu item
while True:
    order = input().capitalize()
    if order in menu:
        print(f"\nThank you {name}, and enjoy your {order}!")
        break  # Exit the loop if the input is valid
    else:
        print(
            f"\nSorry {name}, we don't have {order}. Please choose from the menu: {', '.join(menu)}.\n"
        )
