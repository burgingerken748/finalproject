import random
a = 10
b = 20
c = 30

random_number = random.randint(a,b)
print(random_number)

random.shuffle([a, b, c])
total_sum = a + b + c
print(total_sum)
