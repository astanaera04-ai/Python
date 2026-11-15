# Тапсырма 23. Клиенттер есебі

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

orders_dicts = []
for order in orders:
    d = dict(zip(header, order))
    d["amount"] = d["price"] * d["quantity"]
    orders_dicts.append(d)

# ----- Тапсырманың шешімі -----
def customer_stats(orders):
    """Әр клиенттің тапсырыстары туралы жиынтық ақпаратты қайтарады."""
    stats = {}
    for o in orders:
        info = stats.setdefault(o["customer"], {"orders": 0, "total": 0, "average": 0, "cities": set()})
        info["orders"] += 1
        info["total"] += o["amount"]
        info["cities"].add(o["city"])
    for info in stats.values():
        info["average"] = round(info["total"] / info["orders"], 1)
    return stats


cstats = customer_stats(orders_dicts)

multi_city = [name for name, info in cstats.items() if len(info["cities"]) > 1]
print("Бірнеше қаладан тапсырыс берген:", multi_city)              # ['Dana']

top_spender = max(cstats, key=lambda name: cstats[name]["total"])
print("Ең көп жұмсаған клиент:", top_spender, cstats[top_spender]["total"])   # Arman 44500
