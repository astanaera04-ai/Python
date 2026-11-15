# Тапсырма 26. Санаттар есебі CSV форматында

import csv
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

orders_all, errors = safe_load("orders.txt")

# ----- Тапсырманың шешімі -----
category_report = {}
for o in orders_all:
    info = category_report.setdefault(o["category"], {"category": o["category"], "orders": 0, "quantity": 0, "revenue": 0})
    info["orders"] += 1
    info["quantity"] += o["quantity"]
    info["revenue"] += o["amount"]

rows = sorted(category_report.values(), key=lambda r: r["revenue"], reverse=True)

with open("category_report.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["category", "orders", "quantity", "revenue"])
    writer.writeheader()
    writer.writerows(rows)

with open("category_report.csv", encoding="utf-8") as f:
    report_rows = list(csv.DictReader(f))

for r in report_rows:
    print(r["category"], r["revenue"])

csv_total = sum(int(r["revenue"]) for r in report_rows)
print("CSV қосындысы жалпы түсімге тең бе:", csv_total == sum(o["amount"] for o in orders_all))
