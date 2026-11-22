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

def city_stats(orders):
    stats = {}
    for o in orders:
        info = stats.setdefault(o["city"], {"orders": 0, "revenue": 0, "customers": set()})
        info["orders"] += 1
        info["revenue"] += o["amount"]
        info["customers"].add(o["customer"])
    return stats


stats = city_stats(orders_dicts)
for city, info in stats.items():
    print(f"{city:<10} {info['orders']:>2}  {info['revenue']:>7}  {sorted(info['customers'])}")
