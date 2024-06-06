#!/usr/bin/env python3
"""A script to demonstrate parameters vs. arguments in Python."""

def greet(name="Alice"):
    """Print a greeting message."""
    print(f"Hello, {name}!")

def full_name(first_name, last_name):
    """Print the user's full name."""
    print(f"Your full name is {first_name} {last_name}.")

def print_fruits(*fruits):
    """Print a list of fruits."""
    for fruit in fruits:
        print(fruit)

def main():
    """Execute code at runtime."""
    # Greet the user
    greet()

    # Collect user information
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    full_name(first_name, last_name)

    # Prompt the user to enter fruits
    print("Enter as many fruits as you want (type 'done' to finish):")
    fruits_list = []
    while True:
        fruit = input()
        if fruit.lower() == 'done':
            print("*****  DONE  *****")
            break
        fruits_list.append(fruit)
    
    # Print the fruits entered by the user
    print_fruits(*fruits_list)

if __name__ == "__main__":
    main()

