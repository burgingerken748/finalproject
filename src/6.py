import random

def get_random_python_code():
    # Define a list of Python statements
    statements = ["print('Hello World')", "x = 5", "y = 'hello'"]

    # Get a random index from the list
    random_index = random.randint(0, len(statements) - 1)

    # Return the statement at the random index
    return statements[random_index]