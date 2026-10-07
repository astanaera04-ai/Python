class BankAccount:
    bank_aty = "Казкоммерц Банк"
    jalpy_shot_sany = 0
    minimum_balans = 500
    def __init__(self, ie, baslangy_summa, shot_turi):
        self.ie = ie
        self.balans = baslangy_summa
        self.shot = shot_turi
        BankAccount.jalpy_shot_sany += 1
        self.shot_nomiri = BankAccount.jalpy_shot_sany

    def deposit(self, summa):
        self.balans += summa
        print(f"{summa} тенге салынды. Жана баланыс: {self.balans}")
    def withdraw(self, amount):

        if amount > self.balans - self.minimum_balans:
            print("Қате: балансыңызда жеткілікті қаражат жоқ")
            return False
        else:
            self.balans -= amount
            print(f"{amount} тенге алынды. Жана баланс: {self.balans}")
            return True
    def transfer(self, basga_shot, summa):
        if self.withdraw(summa):
            basga_shot.balans += summa
            print(f"{summa} теңге {basga_shot.ie}-ге аударылды")
        else:
            print("Аудару сәтсіз аяқталды")
print(BankAccount.bank_aty)
Shot1 = BankAccount("Bek1", 500, "жинақ")
Shot2 = BankAccount("Bek2", 1000, "жинақ")
Shot3 = BankAccount("Bek3", 1500, "жинақ")
print(BankAccount.jalpy_shot_sany)
print("Бірінші шот балансы: ", Shot1.balans)
print("Екінші шот баланысы: ", Shot2.balans)
print("Үшінші шот баланысы: ", Shot3.balans)
Shot1.withdraw(500)

BankAccount.bank_aty = "Halyk bank"
print(BankAccount.bank_aty)
Shot1.bank_aty = "BekBoy"
Shot2.bank_aty = "BekBoy2"
print(Shot1.bank_aty)
print(Shot2.bank_aty)












# shot1 = BankAccount("Bek", 5000,"жинақ")
# shot1.deposit(1000)
# shot1.withdraw(100)
# shot2 = BankAccount("Ali", 60000, "жинақ")
# shot3 = BankAccount("Ерлан", 2000, "жинақ")
#
# shot4 = BankAccount("Айгүл", 3000,"ағымдағы" )
# shot4.deposit(5000)
# shot4.withdraw(6000)
#
# shot1.transfer(shot2, 99)
# print(shot1.ie, shot1.balans)
# print(shot2.ie, shot2.balans)
# print(shot3.shot, shot3.balans, shot3.ie)
#
# s = []
# for i in (shot3, shot2, shot1):
#     s.append(i.ie )
#     s.append(i.balans)
# print(s)