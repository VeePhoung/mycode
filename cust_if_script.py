# cust_if_script.py

# Prompt the user to enter the name of a Harry Potter character
character = input("Enter the name of a Harry Potter character (Harry, Hermione, Ron, Draco, Luna, Neville, Cedric, Cho): ").strip().capitalize()

# Define the Hogwarts houses for each character
if character == "Harry":
    house = "Gryffindor"
    description = "Harry Potter is in Gryffindor: Known for bravery, daring, and chivalry. Its emblematic animal is the lion, and its colors are red and gold."
elif character == "Hermione":
    house = "Gryffindor"
    description = "Hermione Granger is in Gryffindor: Known for bravery, daring, and chivalry. Its emblematic animal is the lion, and its colors are red and gold."
elif character == "Ron":
    house = "Gryffindor"
    description = "Ron Weasley is in Gryffindor: Known for bravery, daring, and chivalry. Its emblematic animal is the lion, and its colors are red and gold."
elif character == "Draco":
    house = "Slytherin"
    description = "Draco Malfoy is in Slytherin: Known for ambition, cunning, and resourcefulness. Its emblematic animal is the serpent, and its colors are green and silver."
elif character == "Luna":
    house = "Ravenclaw"
    description = "Luna Lovegood is in Ravenclaw: Known for wisdom, intelligence, and a love for learning. Its emblematic animal is the eagle, and its colors are blue and silver."
elif character == "Neville":
    house = "Gryffindor"
    description = "Neville Longbottom is in Gryffindor: Known for bravery, daring, and chivalry. Its emblematic animal is the lion, and its colors are red and gold."
elif character == "Cedric":
    house = "Hufflepuff"
    description = "Cedric Diggory is in Hufflepuff: Known for loyalty, patience, and a strong work ethic. Its emblematic animal is the badger, and its colors are yellow and black."
elif character == "Cho":
    house = "Ravenclaw"
    description = "Cho Chang is in Ravenclaw: Known for wisdom, intelligence, and a love for learning. Its emblematic animal is the eagle, and its colors are blue and silver."
else:
    description = "Invalid character name. Please enter one of the following: Harry, Hermione, Ron, Draco, Luna, Neville, Cedric, Cho."

# Output the description
print(description)

