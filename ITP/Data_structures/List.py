#1
a = [3, 7, 1, 9, 4, 2]
b = a[0]
for i in a :
    if (i > b):
        b = i
print("Max: ", end="")
print(b)
s = a[0]
for i in a:
    if (i < s):
        s = i
print("Min: ", end="")
print(s)

#2
w = 0
q = [12, 45, 7, 23, 56, 89, 3]
for i in q:
    w += i
print("Task 2" , end = "\n")
print("Қосынды:", w)
print("Орташа:", w / len(q))
#3
print("Task 3")
d = ["алма", "банан", "алмұрт", "жүзім", "апельсин"]
e = []
for i in range(len(d)):
    if (len(d[i]) > 5 ):
        e.append(d[i])
print(e)