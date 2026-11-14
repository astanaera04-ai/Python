a = [12, 5, 27, 8]
def min_max(numbers):
    minn = numbers[0]
    maxx = numbers[0]

    for i in numbers:
        if (i > maxx):
            maxx = i
        if (i < minn):
            minn = i
    return (minn, maxx)
s, b = min_max(a)
print("Ең кіші:", s)
print("Ең үлкен:", b)