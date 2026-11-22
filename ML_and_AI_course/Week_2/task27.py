import json
from orders_data import reset_orders

reset_orders(with_new_orders=True)

def safe_load(path):
    good = []
    bad = []
    with open(path, encoding="utf-8") as f:
        columns = f.readline().strip().split(";")
        for number, line in enumerate(f, start=2):
            line = line.strip()
            if not line:
                continue
            values = line.split(";")
            try:
                values[6] = int(values[6])
                values[7] = int(values[7])
            except ValueError:
                bad.append((number, line))
                continue
            d = dict(zip(columns, values))
            d["amount"] = d["price"] * d["quantity"]
            good.append(d)
    return good, bad

def customer_stats(orders):
    stats = {}
    for o in orders:
        info = stats.setdefault(o["customer"], {"orders": 0, "total": 0, "average": 0, "cities": set()})
        info["orders"] += 1
        info["total"] += o["amount"]
        info["cities"].add(o["city"])
    for info in stats.values():
        info["average"] = round(info["total"] / info["orders"], 1)
    return stats

orders_all, errors = safe_load("orders.txt")

# ----- Тапсырманың шешімі -----
all_cstats = customer_stats(orders_all)

for info in all_cstats.values():
    info["cities"] = sorted(info["cities"])

with open("customers.json", "w", encoding="utf-8") as f:
    json.dump(all_cstats, f, ensure_ascii=False, indent=4)

with open("customers.json", encoding="utf-8") as f:
    customers_data = json.load(f)

for name, info in customers_data.items():
    print(name, info["total"])
