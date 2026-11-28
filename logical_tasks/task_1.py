#print second max number
a = int(input())
# b = []
b = list(map(int, input().split()))

# for i in range(a):
#     s = int(input())
#     b.append(s)

d = b[0]
c = None
s = 0
for i in range(1, a):
    if d < b[i]:
        c = d
        d = b[i]
        s += 1
    if (c is None or c < b[i]) and d != b[i]:
        c = b[i]
        s += 1
if s == 0:
    print(-1)
else:
    print(c)