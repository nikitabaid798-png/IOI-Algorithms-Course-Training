# ---- Office Employee Organiser ----

# STEP 1 - Create a list of employees
employees = ["Rohan", "Ananya", "Karan", "Isha", "Vivek"]
print("Employee list:", employees)

# STEP 2 - Access the list
print("Total employees:", len(employees))
print("First employee:", employees[0])
print("Last employee:", employees[-1])
print("First three employees:", employees[:3])

# STEP 3 - Modify the list
employees.append("Neha")
print("\nAfter adding Neha:", employees)

employees.remove("Vivek")
print("After removing Vivek:", employees)

employees.sort()
print("Sorted alphabetically:", employees)

employees.reverse()
print("Reversed:", employees)

# STEP 4 - Create an employee dictionary
employee = {
    "name": "Mr. Verma",
    "department": "Python Development",
    "experience": 5
}
print("\nEmployee profile:", employee)

# STEP 5 - Dictionary operations
print("Department:", employee["department"])
print("Experience:", employee.get("experience", "Not found"))

employee["experience"] = 6
employee["email"] = "verma@company.com"
employee.pop("experience")

print("Updated employee profile:", employee)

# STEP 6 - Convert lists to an employee directory
employee_ids = [101, 102, 103, 104, 105]
employee_names = ["Rohan", "Ananya", "Karan", "Isha", "Neha"]

employee_directory = dict(zip(employee_ids, employee_names))

print("\nEmployee Directory:", employee_directory)
print("Employee with ID 103:", employee_directory[103])
