def calculate_factorial(number):
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    result = 1
    for i in range(1, number + 1):
        result *= i
    
    return result

number = 5
print(f"The factorial of {number} is {calculate_factorial(number)}")
