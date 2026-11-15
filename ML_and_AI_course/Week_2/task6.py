# Тапсырма 6. Тапсырыс сомалары

from orders_data import reset_orders

# orders.txt бастапқы 10 тапсырыспен қайта жазылады
reset_orders()

# ----- Алдыңғы тапсырмалардан керек деректер -----
with open("orders.txt", encoding="utf-8") as f:
    lines = [line.strip() for line in f]
header = lines[0].split(";")
data_lines = lines[1:]

orders = []
for line in data_lines:
    fields = line.split(";")
    fields[6] = int(fields[6])
    fields[7] = int(fields[7])
    orders.append(fields)

# ----- Тапсырманың шешімі -----
amounts = []

for order in orders:
    amount = order[6] * order[7]
    amounts.append(amount)

print(amounts)
print("Жалпы түсім:", sum(amounts))                              # 141100
print("Ең үлкен сома:", max(amounts))                            # 25000
print("Ең кіші сома:", min(amounts))                             # 7000
print("Орташа сома:", sum(amounts) / len(amounts))               # 14110.0
