# Тапсырма 4. Барлық тапсырыс: тізімдер тізімі

from orders_data import reset_orders

# orders.txt бастапқы 10 тапсырыспен қайта жазылады
reset_orders()

# ----- Алдыңғы тапсырмалардан керек деректер -----
with open("orders.txt", encoding="utf-8") as f:
    lines = [line.strip() for line in f]
header = lines[0].split(";")
data_lines = lines[1:]

# ----- Тапсырманың шешімі -----
orders = []

for line in data_lines:
    fields = line.split(";")
    fields[6] = int(fields[6])     # баға
    fields[7] = int(fields[7])     # дана саны
    orders.append(fields)

print(len(orders))      # 10
print(orders[0])        # ['O101', '2026-10-01', 'Aigerim', 'Almaty', 'Electronics', 'Mouse', 6500, 2]
