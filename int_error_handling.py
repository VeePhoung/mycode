#!/usr/bin/python3
"""Alta3 | TRPatrick
   Rounder - Rounds to the nearest Number
   Demonstrating Error Handling for int() and float()"""

number = input("Pick a number, any number --> ")

def main():
    try:
        print(int(float(number)))
    except ValueError:
        print("Cannot convert non-numeric string to an integer.")

if __name__ == "__main__":
    main()

