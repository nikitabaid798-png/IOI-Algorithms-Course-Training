# Ask the user to enter the total number of classes
total_classes = int(input("Enter total number of classes: "))

# Ask the user to enter the number of classes attended
attended_classes = int(input("Enter number of classes attended: "))

# Calculate the attendance percentage
attendance_percentage = (attended_classes / total_classes) * 100

# Display the attendance percentage
print("Your attendance is:", attendance_percentage, "%")

# Check exam eligibility
if attendance_percentage >= 75:
    print("You are eligible to appear for the exam.")
else:
    print("You are not eligible to appear for the exam.")
