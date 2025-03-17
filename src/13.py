import random

def get_random_code():
    # Generate a random integer between 1 and 9
    random_int = random.randint(1, 9)
    # Use the random integer to determine the code
    if random_int == 1:
        return "ACME"
    elif random_int == 2:
        return "ABC"
    elif random_int == 3:
        return "DEF"
    elif random_int == 4:
        return "GHI"
    elif random_int == 5:
        return "JKL"
    elif random_int == 6:
        return "MNO"
    elif random_int == 7:
        return "PQR"
    elif random_int == 8:
        return "STU"
    elif random_int == 9:
        return "VWX"
