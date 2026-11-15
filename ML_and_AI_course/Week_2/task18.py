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

category_revenue = {}

for o in orders_dicts:
    category_revenue[o["category"]] = category_revenue.get(o["category"], 0) + o["amount"]
print(category_revenue)
total = sum(category_revenue.values())

for category, revenue in category_revenue.items():
    share = revenue / total * 100
    print(f"{category:<12} {revenue:>7}  {share:.1f}%")
