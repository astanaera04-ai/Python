#task 1
def qosu(a, b):
    return a + b
print(qosu(1, 5))

#task 2
def kvadrat(san):
    return pow(san, 2)
print(kvadrat(5))

#task 3
def salemdesu(aty):
    return f"Сәлем, {aty}!"
print(salemdesu("Bek"))

#task 4
def max_taby(a, b, c):
    return max(a, b, c)
print(max_taby(1, 2, 3))

#task 5
import random
def random_s(s):
    a = []
    for i in range(s):
        a.append(random.randint(1, 100))
    return a
print(random_s(5))