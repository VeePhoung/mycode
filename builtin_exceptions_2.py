#!/usr/bin/python3
"""Alta3 | TRPatrick
   Built-In Exceptions"""

def calculate_area(radius):
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number")
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return 3.14 * radius * radius

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

    try:
        len(5)
    except TypeError:
        print("Wrong type passed to a function!")

    try:
        int("abc")
    except ValueError:
        print("Invalid value to convert to integer!")

    try:
        print(calculate_area(-5))
    except TypeError as e:
        print(f"TypeError: {e}")
    except ValueError as e:
        print(f"ValueError: {e}")

if __name__ == "__main__":
    main()

