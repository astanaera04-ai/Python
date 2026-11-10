class Transaction:
    def __init__(self, turi, summa):
        self.turi = turi
        self.summa = summa

    def __str__(self):
        return f"{self.turi}: {self.summa} тенге "


class BankAccount :
    bank_aty = "Казкоммерц Банк"
    jalpy_shot_sany = 0
    minimum_balans = 500

    def __init__(self, ie, baslangy_summa, shot_turi):
        self.ie = ie
        if baslangy_summa < 0:
            raise ValueError("Бастапқы сумма 0 ден төмен")
        self.balans = baslangy_summa
        self.shot = shot_turi
        BankAccount.jalpy_shot_sany += 1
        self.shot_nomiri = BankAccount.jalpy_shot_sany
        self.tarih = []

    def deposit(self, summa):
        #------------raise ---------------
        if summa <= 0:
            raise ValueError("Сумма 0 ден үлкен болу керек")

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

    def payyz_qosu(self):
        print("Бұл шотта пайыз жоқ")


class SavingAccount(BankAccount):
    def __init__(self, ie,balans , shot_turi, payyz):
        super().__init__(ie, balans, shot_turi)
        self.payyz = payyz

    def payyz_qosu(self):
        self.balans *= ( self.payyz / 100 + 1 )
        print("Пайыз косылгандагы сумма", round(self.balans, 1))



class CheckingAccount(BankAccount):

    def __init__(self, ie,  baslangy_summa, shot_turi, komissiya):
        super().__init__(ie, baslangy_summa, shot_turi)
        self.komissiya = komissiya

    def withdraw(self, amount):
        return super().withdraw(amount + self.komissiya)


t = Transaction("deposit", 200)
print(t)
s = BankAccount("A", 1000, "жинақ")
print(s.balans)




# Ch = CheckingAccount("Medi", 2000, "j", 50)
# print(Ch.withdraw(100))
# Ch2 = CheckingAccount("Medi2", 100000, "j", 150)
# print(Ch2.withdraw(500))
#
# Ch3 = CheckingAccount("Aru", 600, "j", 50)
# print(Ch3.withdraw(100))
#
#
# Shot5 = [BankAccount("Bek1", 500, "жинақ"), SavingAccount("Medi2", 5000, "жинақ", 10)]
# for i in Shot5:
#     i.payyz_qosu()
#
# # # print(BankAccount.bank_aty)
# Shot1 = BankAccount("Bek1", 500, "жинақ")
# Shot2 = BankAccount("Bek2", 1000, "жинақ")
# Shot3 = BankAccount("Bek3", 1500, "жинақ")
#
# shottar = [
#     BankAccount("a", 2000, "j"),
#     SavingAccount("B", 5000, "j", 50),
#     CheckingAccount("S", 9900, "j", 25)
# ]
# for i in shottar:
#     i.withdraw(55)
#






# #------------exception---------
# try:
#     Shot1.deposit(-100)
# except ValueError as e:
#     print("Қате- ", e, end="\n")
#
#
# try:
#     Shot4 = BankAccount("Medi",-100, "Жинақ")
# except ValueError as e:
#     print("Қате- ",e)
#
#
# print(BankAccount.jalpy_shot_sany)




# print(BankAccount.jalpy_shot_sany)
# print("Бірінші шот балансы: ", Shot1.balans)
# print("Екінші шот баланысы: ", Shot2.balans)
# print("Үшінші шот баланысы: ", Shot3.balans)
# Shot1.withdraw(500)
#
# BankAccount.bank_aty = "Halyk bank"
# print(BankAccount.bank_aty)
# Shot1.bank_aty = "BekBoy"
# Shot2.bank_aty = "BekBoy2"
# print(Shot1.bank_aty)
# print(Shot2.bank_aty)


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