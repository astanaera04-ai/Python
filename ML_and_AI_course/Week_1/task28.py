num = [12, -5, 8, 0, -3, 17, 4, 0, -9]
n = 0
o = 0
t = 0
for i in num:
    if (i == 0):
        n += 1
    elif(i > 0):
        o += 1
    else:
        t += 1
print("nol: ", n)
print("on: ", o)
print("ter: ", t)