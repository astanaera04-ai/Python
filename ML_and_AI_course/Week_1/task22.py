a = float(input("a қабырғасын енгізіңіз: "))
b = float(input("b қабырғасын енгізіңіз: "))
c = float(input("c қабырғасын енгізіңіз: "))

if (a + b > c) and (a + c > b) and (b + c > a):

    if a == b == c:
        print("Тең қабырғалы үшбұрыш")
    elif a == b or b == c or a == c:
        print("Теңбүйірлі үшбұрыш")
    else:
        print("Әртүрлі қабырғалы үшбұрыш")

else:
    print("Мұндай үшбұрыштың болуы мүмкін емес")
