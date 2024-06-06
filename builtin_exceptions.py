#!/usr/bin/python3
"""Alta3 | TRPatrick
   Built-In Exceptions"""

def main():
    """Code executed at Runtime"""
    try:
        input("Press Enter to continue or Ctrl+C to interrupt...")
    except KeyboardInterrupt:
        print("Operation interrupted by the user.")

    try:
        result = 10 / 0
    except ArithmeticError:
        print("Cannot divide by zero!")

    my_list = [1, 2, 3]

    try:
        print(my_list[3])
    except IndexError:
        print("That index is out of bounds!")

    my_dict = {"name": "Alice"}

    try:
        print(my_dict["age"])
    except KeyError:
        print("The key does not exist!")

if __name__ == "__main__":
    main()

