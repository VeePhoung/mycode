#!/usr/bin/python3
"""Calculate User BMI using Input Variables"""
 
def calculate_bmi(weight, height):
    """Function to calculate BMI"""
    bmi = (weight / (height ** 2)) * 703
    return bmi
 
def determine_bmi_category(bmi):
    """Determine BMI category"""
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obesity"
    return category
 
def main():
    """Collect User Input"""
    weight = float(input("Enter your weight in pounds: "))
    height = float(input("Enter your height in inches: "))
 
    # Calculate BMI
    bmi = calculate_bmi(weight, height)
    category = determine_bmi_category(bmi)
 
    # Display the results
    print(f"Your BMI is {bmi:.2f}, which is considered '{category}'.")
 
if __name__ == "__main__":
    main()

