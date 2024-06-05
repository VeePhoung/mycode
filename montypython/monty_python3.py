#!/usr/bin/python3
"""Alta3 Research | RZFeeser
  Conditionals - Life of Brian guessing game without a while True loop."""

answer = input('Enter your guess: ')
if answer.lower() == "shrubbery":
    print("You gave the super secret answer!")
    exit()

round = 0
answer = ""

while round < 3 and answer.lower() != "brian":
    round += 1     # increase the round counter by 1
    answer = input('Finish the movie title, "Monty Python\'s The Life of ______": ')
    if answer.lower() == "brian": # convert both the user's input and the correct answer to lowercase
        print("Correct!")
    elif round == 3:    # logic to ensure round has not yet reached 3
        print("Sorry, the answer was Brian.")
    else:                 # if answer was wrong
        print("Sorry. Try again!")

