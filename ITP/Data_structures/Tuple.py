#1
print("Task 1")
a = (38.5, 68.3)
s,d = a
if (s > 37):
    print("temp higher than 37" )
else:
    print("temp lower than 37" )

#2
print("Task 2")
q = [("Асан", 85), ("Дана", 92), ("Ерлан", 78)]
e = q[0]
for i in range(1, len(q)):
    if (q[i][1] > e[1]):
        e = q[i]
print("Smartest student: ", e[0], e[1])