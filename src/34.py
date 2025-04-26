import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Example usage:
number = 37  # Change this to any number you want to check for primality
if is_prime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")
