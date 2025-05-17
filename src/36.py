import random

def get_random_string(length):
    """
    Generate a random string of a given length.
    
    Parameters:
        length (int): The length of the string to generate.
        
    Returns:
        str: A randomly generated string.
    """
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(length))

# Example usage
random_string = get_random_string(10)
print(random_string)
