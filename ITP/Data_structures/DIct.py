#task 1
adam = {"aty": "Asan", "jasy" : 25, "qala" : "Astana"}
adam["jasy"] = 26
adam["job"] = "in"
adam.get("aty")
for kit in adam:                    # тек киттерді береді
    print(kit)

for man in adam.values():            # тек мәндерді береді
    print(man)

for kit, man in adam.items():        # екеуін бірге береді (ЕҢ ЖИІ ҚОЛДАНЫЛАДЫ)
    print(kit, "->", man)

#task 2
tauarlar = {"нан": 150, "сүт": 400, "жұмыртқа": 900, "май": 1200}
a = 0
for i , j in tauarlar.items():
    a +=j
print("Sum" , a)

#task 3
s = {}
m = "pythonpp"
for i in m:
    s[i] = s.get(i, 0) + 1
print(s)

#task 3
ee = {"Асан": 85, "Дана": 92, "Ерлан": 78, "Мадина": 95}
tt = 0
rr = {}
for i, e in ee.items():
    tt += e
tt = tt / len(ee)
for i, e in ee.items():
    if (tt > e):
        rr[i] = e
print(rr)

#task 4
