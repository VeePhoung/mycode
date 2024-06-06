#!/usr/bin/env python3
"""Alta3 | TRPatrick
   Demonstration of Advanced Function Features"""

# Global variables
x = "This variable is being set globally"
y = 10

# Function to demonstrate shadowing
def shadow_example(y):
    print("Inside shadow_example, y =", y)

# Function to demonstrate scope
def test_scope():
    x = "This variable is being set locally"
    print("Inside test_scope:", x)

# Function with a default argument
def print_greeting(message="Hello, World!"):
    print(message)

# Main function
def main():
    # Call print_greeting with the default message
    print_greeting()
    # Call print_greeting with a custom message
    print_greeting("Hello Function!")
    
    # Call test_scope to see the effect of local variable x
    test_scope()
    # Print the global variable x
    print("Outside function:", x)
    
    # Call shadow_example to see the effect of passing y
    shadow_example(y)

# Check if the script is being run directly
if __name__ == "__main__":
    main()

