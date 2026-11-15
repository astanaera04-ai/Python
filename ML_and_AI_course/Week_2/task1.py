# Тапсырма 1. Файлды оқу

from orders_data import reset_orders

# orders.txt бастапқы 10 тапсырыспен қайта жазылады
reset_orders()

# ----- Тапсырманың шешімі -----
with open("orders.txt", encoding="utf-8") as f:
    lines = []
    for line in f:
        lines.append(line.strip())

for line in lines:
    print(line)
print("Жолдар саны:", len(lines))          # 11
