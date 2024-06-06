#!/usr/bin/python3
"""Alta3 | TRPatrick
   Demonstrating Positional Arguments"""

def display_info(name, age):
    print(f"Name: {name}, Age: {age}")

def main():
    display_info(age=30, name="Alice")

if __name__ == "__main__":
    main()

