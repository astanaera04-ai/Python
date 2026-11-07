q = int(input())
def fib(x):
    s = [0, 1]
    a = 0
    b = 1

    c = 0
    for i in range(x - 2):
        c = a + b
        a = b
        b = c
        s.append(c)
    print(s)
fib(q)