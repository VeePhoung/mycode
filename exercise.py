#!/usr/bin/env python3
"""Alta3 Research | TPatrick
   Lists Challenge"""

# Import the random module
import random

def main():
    # Create a list of words related to coding
    wordbank = ["indentation", "spaces"]

    # Create a list of student names
    tlgstudents = ["Aaron", "Andy", "Brent", "Cedric", "Chris", "Etien",
                   "Franco", "John", "Joey", "Jordan", "Penn", "Samuel",
                   "Sanam", "Zachary"]

    # Print the list of students
    print("List of students:")
    print(tlgstudents)
    
    # Add the number 4 to the wordbank list
    wordbank.append(4)
    print("Updated wordbank list:")
    print(wordbank)
    
    # Ask the user to enter a number between 1 and 14
    num = input("Enter a student number between 1 and 14: ")
    
    # Convert the input to an integer
    num = int(num)
    
    # Get the student name based on the number entered
    name = tlgstudents[num - 1]  # Subtract 1 to match the list index
    print(f"Your chosen student is {name}.")
    print(f"{name} always uses {wordbank[2]} {wordbank[1]} to indent.")
    
    # Randomly select a student name from the list
    random_name = random.choice(tlgstudents)
    print(f"Randomly selected student: {random_name}")

if __name__ == "__main__":
    main()

