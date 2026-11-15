# Тапсырма 20. Қысқаша есепті файлға жазу

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

orders_dicts = []
for order in orders:
    d = dict(zip(header, order))
    d["amount"] = d["price"] * d["quantity"]
    orders_dicts.append(d)

unique_customers = set(customers)
order_count = {}
for o in orders_dicts:
    order_count[o["customer"]] = order_count.get(o["customer"], 0) + 1

# ----- Тапсырманың шешімі -----
total_revenue = sum(o["amount"] for o in orders_dicts)

with open("summary.txt", "w", encoding="utf-8") as f:
    f.write(f"Тапсырыстар саны: {len(orders_dicts)}\n")
    f.write(f"Жалпы түсім: {total_revenue}\n")
    f.write(f"Орташа сома: {total_revenue / len(orders_dicts)}\n")
    f.write(f"Бірегей клиенттер саны: {len(unique_customers)}\n")
    f.write(f"Ең белсенді клиент: {max(order_count, key=order_count.get)}\n")

with open("summary.txt", encoding="utf-8") as f:
    print(f.read())
