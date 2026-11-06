word =input()

a = word.split(" ")
print(a)
def count_words(text):
    i = 0
    for j in text:
        if j != '':
            i += 1
    print(i)
count_words(a)