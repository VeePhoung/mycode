#!/usr/bin/python3
""" Alta3 | TRPatrick
    Perform Binary Multiplication"""
  
def binary_multiplication(binary1, binary2):
    # Convert binary strings to decimal
    decimal1 = int(binary1, 2)
    decimal2 = int(binary2, 2)
  
    # Perform multiplication in decimal
    result_decimal = decimal1 * decimal2
  
    # Convert the result back to binary
    result_binary = bin(result_decimal)[2:]  # [2:] to remove the '0b' prefix
  
    return result_binary
  
def main():
    binary1 = '1011'  # Example binary number 1
    binary2 = '110'   # Example binary number 2
  
    result = binary_multiplication(binary1, binary2)
    print(f"The binary multiplication of {binary1} and {binary2} is: {result}")
  
if __name__ == "__main__":
    main()

