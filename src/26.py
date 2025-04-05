import os

def write_random_file(filename):
    """
    This function generates a random string and writes it to a file.
    The filename can be any valid path on your system.
    """
    # Generate a random string of 10 characters
    random_string = os.urandom(10)
    
    # Write the random string to the specified file
    with open(filename, 'w') as f:
        f.write(random_string)

# Example usage: write_random_file("random_data.txt")
