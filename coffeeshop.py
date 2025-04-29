#!/bin/python3

import time

menu = "Black coffee, Cappuccino, Latte, Espresso"

print("Hello stranger\n" + "Welcome to our Coffee shop!\n")

name = input("What is your name? ").capitalize()

print("\nHello " + name + " nice to see you here!")

time.sleep(1)

print(
    "\nHey "
    + name
    + " what would you like?\n"
    + "Here is our menu: "
    + menu
    + "."
    + "\nAnything you like?\n"
)

order = input()
