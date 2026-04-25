def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return 'Error: Division by zero'
    return a / b

# Examples
print('Addition: 10 + 20 =', add(10, 20))
print('Subtraction: 20 - 10 =', subtract(20, 10))
print('Multiplication: 10 * 20 =', multiply(10, 20))
print('Division: 20 / 10 =', divide(20, 10))
print('Division by zero: 10 / 0 =', divide(10, 0))
