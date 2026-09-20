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

#3
w = ("Астана", 2026, "қыс")
e, r, t = w
print("City: " , e, "Year: ", r, "Seson: ", t)

#4
p = [("Астана", -15), ("Алматы", 2), ("Шымкент", 8), ("Атырау", -5), ("Көкшетау", -18)]
tt = p[0]
for i in range(len(p)):
    if(p[i][1] > tt[1]):
        tt = p[i]
print("Name: ", tt[0], "C: ", tt[1])

#4
aa = (5, 3)
qq, ww = aa
print("Area: ", qq * ww, "P: ", 2 * (qq + ww))