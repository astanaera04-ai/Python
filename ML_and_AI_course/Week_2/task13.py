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

orders_dicts = []
for order in orders:
    d = dict(zip(header, order))
    d["amount"] = d["price"] * d["quantity"]
    orders_dicts.append(d)

print(orders_dicts)

sorted_orders = sorted(orders_dicts, key=lambda o: o["amount"], reverse=True)
print(sorted_orders)

top3 = sorted_orders[:3]

for o in top3:
    print(f"{o['order_id']}  {o['customer']:<8} {o['product']:<12} {o['amount']:>7}")
