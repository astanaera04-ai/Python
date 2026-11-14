point = (3, 7)
x, y = point
print("x =", x)
print("y =", y)

try:
    point[0] = 1
except TypeError as e:
    print("Қате:", e)