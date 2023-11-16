# take the first number from user.
# take the operation from the user.
# take the second number from user.
# create function to calculate the result.
# print the result for the user
def calculate(first_number, operation, second_number):
    if operation == "+":
        return first_number + second_number
    elif operation == "-":
        return first_number - second_number
    elif operation == "*":
        return first_number * second_number
    elif operation == "/":
        if second_number == 0:
            return "Divided by zero"
        return first_number / second_number
    else:
        return "Invalid operation"


one = float(input("Enter the first number: "))
while True:
    operation = input("Enter the operation ( +, -, *, / ): ")
    if operation in ["+", "-", "*", "/"]:
        break
    else:
        print("Invalid operation. Please enter one of the following: +, -, *, /")
two = float(input("Enter the second number: "))

result = calculate(one, operation, two)
print("Result:", result)