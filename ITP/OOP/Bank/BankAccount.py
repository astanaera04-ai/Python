class BankAccount:
    def __init__(self, ie, baslangy_summa, shot_turi):
        self.ie = ie
        self.balans = baslangy_summa
        self.shot = shot_turi
    def deposit(self, summa):
        self.balans += summa
        print(f"{summa} тенге салынды. Жана баланыс: {self.balans}")
    def withdraw(self, amount):
        if amount > self.balans:
            print("Қате: балансыңызда жеткілікті қаражат жоқ")
        else:
            self.balans -= amount
            print(f"{amount} тенге алынды. Жана баланс: {self.balans}")

shot1 = BankAccount("Bek", 5000,"жинақ")
shot1.deposit(1000)
shot1.withdraw(100)
shot2 = BankAccount("Ali", 6000, "жинақ")
shot3 = BankAccount("Ерлан", 2000, "жинақ")

# print(shot1.ie, shot1.balans)
# print(shot2.ie, shot2.balans)
# print(shot3.shot, shot3.balans, shot3.ie)
#
# s = []
# for i in (shot3, shot2, shot1):
#     s.append(i.ie )
#     s.append(i.balans)
# print(s)