import random

def get_random_code():
    """Generate a random 8-digit code"""
    return ''.join(str(random.randint(0, 9)) for _ in range(8))