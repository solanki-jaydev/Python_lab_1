def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b == 0:
        return "Error: Division by zero!"
    else:
        return a / b

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

sum_result = add_numbers(num1, num2)
difference_result = subtract_numbers(num1, num2)
product_result = multiply_numbers(num1, num2)
division_result = divide_numbers(num1, num2)

print(f"Addition: {num1} + {num2} = {sum_result}")
print(f"Subtraction: {num1} - {num2} = {difference_result}")
print(f"Multiplication: {num1} * {num2} = {product_result}")
print(f"Division: {num1} / {num2} = {division_result}")
