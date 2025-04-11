import random

def get_random_int(min_value: int, max_value: int) -> int:
    """
    This function generates a random integer between min_value and max_value.
    It's important to note that this implementation is not error-free,
    but it should be sufficient for many cases.

    Args:
        min_value (int): The minimum value of the range (inclusive).
        max_value (int): The maximum value of the range (exclusive).

    Returns:
        int: A random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)

# Example usage
min_value = 1
max_value = 50
random_int = get_random_int(min_value, max_value)
print(f"Random Int: {random_int}")
