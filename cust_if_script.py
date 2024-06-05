# cust_if_script.py

# Prompt the user for a number (1 through 4)
house_number = int(input("Enter a number (1 through 4) to select a Hogwarts house: "))

# Define the houses and their descriptions
if house_number == 1:
    house = "Gryffindor"
    description = "Gryffindor: Known for bravery, daring, and chivalry. Its emblematic animal is the lion, and its colors are red and gold."
elif house_number == 2:
    house = "Hufflepuff"
    description = "Hufflepuff: Known for loyalty, patience, and a strong work ethic. Its emblematic animal is the badger, and its colors are yellow and black."
elif house_number == 3:
    house = "Ravenclaw"
    description = "Ravenclaw: Known for wisdom, intelligence, and a love for learning. Its emblematic animal is the eagle, and its colors are blue and silver."
elif house_number == 4:
    house = "Slytherin"
    description = "Slytherin: Known for ambition, cunning, and resourcefulness. Its emblematic animal is the serpent, and its colors are green and silver."
else:
    description = "Invalid number. Please enter a number between 1 and 4."

# Output the house and description
print(description)

