#!/usr/bin/python3
"""Alta3 | TRPatrick
   Numeral System Conversions"""

# Gather Input
number = input("Enter your number: ")
base = int(input("Enter the base of the number (2, 8, 10, 16): "))

def main():
    """Perform the Numeral System Conversion"""
    # Determine which formula to use
    if base == 2:
        decimal = int(number, 2)
    elif base == 8:
        decimal = int(number, 8)
    elif base == 10:
        decimal = int(number)
    elif base == 16:
        decimal = int(number, 16)
    else:
        print("Invalid base")
        exit() # Gracefully terminate the script

    # print the conversions to the user
    print(f"Binary: {bin(decimal)}")
    print(f"Octal: {oct(decimal)}")
    print(f"Decimal: {decimal}")
    print(f"Hexadecimal: {hex(decimal)}")

if __name__ == "__main__":
    main()

