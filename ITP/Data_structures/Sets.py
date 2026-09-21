# #task 1
# topA = {"Асан", "Дана", "Ерлан"}
# topB = {"Дана", "Мадина", "Ерлан"}
# topC = set()
# topAA = set()
# topBB = set()
# for i in topA:
#     if (i in topB):
#         topC.add(i)
#     if (i not in topB):
#         topAA.add(i)
# for i in topB:
#     if (i not in topA):
#         topBB.add(i)
# print(topC)
# print(topAA)
# print(topBB)
#
# #task 2
# q = [5, 2, 8, 2, 5, 9, 8, 1]
# w = set(q)
# print (len(w))
#

#task 3
e = {"Асан": ["математика", "физика"], "Дана": ["физика", "химия"], "Ерлан": ["математика", "химия"]}
ee = {}
for i, j in e.items():
    for sab in j:
        ee[sab] = ee.get(sab, 0) + 1
en_kop_sabak = None
en_kop_san = 0

for sabak, san in ee.items():
    if san > en_kop_san:
        en_kop_san = san
        en_kop_sabak = sabak

print("Ең көп алынатын сабақ:", en_kop_sabak, "-", en_kop_san, "студент")