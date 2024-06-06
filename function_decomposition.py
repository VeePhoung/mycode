#!/usr/bin/python3
"""Alta3 | TRPatrick
   Building User-Defined Functions"""

# User-defined function
def greet(name):
    print(f"Hello, {name}!")

def add(a, b):
    return a + b

def print_message():
    print("This function returns None.")

def main():
    greet(input("What is your name? "))

    result = add(5, 3)
    print("5 + 3 =", result)

    print("Function result:", print_message())

if __name__ == "__main__":
    main()

