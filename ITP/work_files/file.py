import os
os.makedirs("data", exist_ok = True)
print("Ағымдағы бума:", os.getcwd())
print("data бумасы бар ма:", os.path.exists("data"))

# Файлға жазу

f = open("data/hello.txt", "w", encoding="utf-")
f.write("jnefodnson\n")
f.write("jnefodnsoncssdcsssscdscs\n")
f.close()
print("done")

# with операторы
with open('data/helllo.txt',"w", encoding="utf-") as f:
    f.write("rfnvoinoibgdim")
    f.write("rfnvoinoibgdimdrsvfopmrms")
print("done2")


cities = ["Almaty", "Astana", "Shymkent", "Karaganda", "Aktobe"]

with open("data/cities.txt", "w", encoding="utf-8") as f:
    for city in cities:
        f.write(city + "\n")

# writelines(): дайын жолдар тізімін бірден жазу
lines = ["бірінші жол\n", "екінші жол\n", "үшінші жол\n"]

with open("data/lines.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)

# Файлды оқу

# read(): бүкіл мазмұнды оқу
with open("data/hello.txt", "r", encoding="utf-8") as f:
    content = f.read()

print(content)

# readline(): жолдарды бір-бірлеп оқу
with open("data/cities.txt", encoding="utf-8") as f:
    first_line = f.readline()
    second_line = f.readline()

print(repr(first_line))
print(repr(second_line))

# Файлмен жұмыс кезіндегі қателерді өңдеу
try:
    with open("data/missing.txt", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("Файл табылмады")
    
# Файлдың бар-жоғын алдын ала тексеру
path = "data/scores.txt"

if os.path.exists(path):
    print(path, "бар, өлшемі:", os.path.getsize(path), "байт")
else:
    print(path, "жоқ")

# Файлдағы қате деректі өткізіп жіберу
with open("data/mixed.txt", "w", encoding="utf-8") as f:
    f.write("10\n20\nжиырма бес\n30\n")

valid = []
with open("data/mixed.txt", encoding="utf-8") as f:
    for line in f:
        try:
            valid.append(int(line))
        except ValueError:
            print("Санға айналмады:", line.strip())

print(valid)