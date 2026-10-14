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
            print("Бүтін сан жаз")

# jas = get_jas()
# print(jas)

#3
def main():
    x = get_jas()
    print(f"x is {x}")
main()