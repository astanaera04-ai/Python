text = input()
def is_palindrome(a):
    b = a.replace(" ", "")
    c = b[::-1]
    if (b == c):
        print("true")
    else:
        print("false")
is_palindrome(text)