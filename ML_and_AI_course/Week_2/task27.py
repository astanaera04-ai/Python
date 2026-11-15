# Тапсырма 27. Клиенттер базасы JSON форматында

import json
from orders_data import reset_orders

# 24-тапсырмадан кейінгі күй: бастапқы 10 тапсырыс + 3 жаңа жол
reset_orders(with_new_orders=True)

# ----- Алдыңғы тапсырмалардан керек деректер -----
def safe_load(path):
    """Қате жолдарды өткізіп, (тапсырыстар, қателер) кортежін қайтарады."""
    good = []
    bad = []
    with open(path, encoding="utf-8") as f:
        columns = f.readline().strip().split(";")
        for number, line in enumerate(f, start=2):    # тақырып 1-жол, деректер 2-ден басталады
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

orders_all, errors = safe_load("orders.txt")

# ----- Тапсырманың шешімі -----
all_cstats = customer_stats(orders_all)

for info in all_cstats.values():
    info["cities"] = sorted(info["cities"])      # жиын JSON-ға жазылмайды, тізімге айналдырамыз

with open("customers.json", "w", encoding="utf-8") as f:
    json.dump(all_cstats, f, ensure_ascii=False, indent=4)

with open("customers.json", encoding="utf-8") as f:
    customers_data = json.load(f)

for name, info in customers_data.items():
    print(name, info["total"])                   # Nurlan 66500
