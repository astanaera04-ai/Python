from orders_data import reset_orders

reset_orders()

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
customers = []

for order in orders:
    customers.append(order[2])

print(customers)
print("Ұзындығы:", len(customers))
print("Бірінші:", customers[0], "соңғы:", customers[-1])
print("Aigerim:", customers.count("Aigerim"))       # 3
