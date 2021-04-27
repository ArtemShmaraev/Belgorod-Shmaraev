from random import randint

x = randint(3, 25)
print(x)
for i in range(x):
    a = randint(1, 1000)
    b = randint(a, 1200)
    print(a, b)
