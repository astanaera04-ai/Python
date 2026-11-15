# Тапсырма 2. Тақырып жолын бөлу

from orders_data import reset_orders

# orders.txt бастапқы 10 тапсырыспен қайта жазылады
reset_orders()

# ----- Алдыңғы тапсырмалардан керек деректер -----
with open("orders.txt", encoding="utf-8") as f:
    lines = [line.strip() for line in f]

# ----- Тапсырманың шешімі -----
header = lines[0].split(";")
data_lines = lines[1:]

for number, column in enumerate(header, start=1):
    print(number, column)

print("Тапсырыстар саны:", len(data_lines))   # 10
