# Ask the user to enter their weight in kilograms
weight = float(input("Enter your weight in kg: "))

# Ask the user to enter their height in meters
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Display the BMI
print("Your BMI is:", round(bmi, 2))

# Check the BMI category
if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obesity")
