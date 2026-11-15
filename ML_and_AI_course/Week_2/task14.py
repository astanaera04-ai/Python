# Тапсырма 14. Кортеждер тізімі және zip

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

customers = [order[2] for order in orders]

amounts = [order[6] * order[7] for order in orders]

# ----- Тапсырманың шешімі -----
pairs = list(zip(customers, amounts))
print(pairs)

best_customer = ""
best_amount = 0

for customer, amount in pairs:
    if amount > best_amount:
        best_amount = amount
        best_customer = customer

print("Ең ірі тапсырыс:", best_customer, best_amount)     # Arman 25000
