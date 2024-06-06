#!/usr/bin/env python3

import random

# Define a list of words related to coding
wordbank = ["indentation", "spaces"]

# Define a list of student names
tlgstudents = ["Aaron", "Andy", "Brent", "Cedric", "Chris", "Etien", "Franco", "John", "Joey", "Jordan", "Penn", "Samuel", "Sanam", "Zachary"]

# Add the number 4 to the wordbank list
wordbank.append(4)

# Ask the user to enter a number between 0 and 14
num = input("Please enter a number between 0 and 14: ")

# Convert the user input from a string to an integer
num = int(num)

# Randomly select a student name from the list
random_student = random.choice(tlgstudents)

# Print a message using the selected student name and elements from the wordbank list
print(f"{random_student} always uses {wordbank[-1]} {wordbank[1]} to indent.")

