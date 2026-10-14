# int("abc")        # ValueError: мәтінді санға айналдыра алмайды
# 10 / 0            # ZeroDivisionError
# [1, 2, 3][5]      # IndexError: индекс жоқ
# {"a": 1}["b"]     # KeyError: кілт жоқ
# open("жоқ.txt")   # FileNotFoundError (сенде address.txt-пен болған қате)
# print(x)          # NameError: x жарияланбаған

#1
try:
    x = int(input("What's x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")

#2
def get_jas():
    while True:
        try:
            return int(input("Жас: "))
        except ValueError:
            # print("Бүтін сан жаз")
            pass

# jas = get_jas()
# print(jas)

#3
def main():
    x = get_jas()
    print(f"x is {x}")
main()