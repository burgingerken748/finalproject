import random

def get_random_code(length=8):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '-', '+', '=', '(', ')', '{', '}', '[', ']', ';', ':', "'", '"', '<', '>', ',', '.', '/', '?']
    all_chars = letters + numbers + symbols
    random_code = ''.join(random.choice(all_chars) for _ in range(length))
    return random_code