a = [3, 8, 11, 20, 7]
def is_even(a):
    for i in a:
        if (i % 2 == 0):
            print(i, "it is even")
        else:
            print(i, "it is odd")
is_even(a)