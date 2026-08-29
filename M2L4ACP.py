# ---- Expression Class ----

class Expression:

    # STEP 1 - Constructor
    def __init__(self, number1, number2, operator):
        self.number1 = number1
        self.number2 = number2
        self.operator = operator
        print("Expression created!")

    # STEP 2 - Display the expression
    def display(self):
        print("Expression:", self.number1, self.operator, self.number2)

    # STEP 3 - Calculate the result
    def calculate(self):
        if self.operator == "+":
            return self.number1 + self.number2
        elif self.operator == "-":
            return self.number1 - self.number2
        elif self.operator == "*":
            return self.number1 * self.number2
        elif self.operator == "/":
            return self.number1 / self.number2

    # STEP 4 - Destructor
    def __del__(self):
        print("Expression deleted.")


# STEP 5 - Take input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

# STEP 6 - Create an object
my_expression = Expression(num1, num2, operator)

# STEP 7 - Use the class methods
my_expression.display()
print("Result:", my_expression.calculate())

# STEP 8 - Delete the object
del my_expression
