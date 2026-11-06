prices = {"notebook": 450, "pen": 120, "backpack": 8500, "ruler": 200}
b = 0
s = 0
q = {}
for i, j in prices.items():
    b += j
    if(s < j):
        s = j
        q[0] = i, j
print(b)
s,d = q[0]
print(s, d)