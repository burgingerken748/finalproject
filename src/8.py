import random
def get_random_code():
    numbers = ["1", "2", "3", "4", "5", "6"]
    operators = ["+", "-", "*", "/", "%"]
    variables = ["x", "y", "z"]
    expressions = []
    for i in range(3):
        expression = ""
        for j in range(random.randint(2, 4)):
            if j == 0:
                expression += variables[random.randint(0, 2)]
            else:
                expression += operators[random.randint(0, 3)]
            expression += numbers[random.randint(0, 5)]
        expressions.append(expression)
    return expressions