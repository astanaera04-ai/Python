items = [3, 7, 3, 1, 9, 7, 1, 5]
a = []
for i in range(len(items)):
    if (items[i] not in a):
        a.append(items[i])
print(a)