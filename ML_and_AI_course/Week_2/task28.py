# Тапсырма 28. Қалалар бойынша жеке файлдар

import os
from orders_data import reset_orders

# 24-тапсырмадан кейінгі күй: бастапқы 10 тапсырыс + 3 жаңа жол
reset_orders(with_new_orders=True)

# ----- Алдыңғы тапсырмалардан керек деректер -----
with open("orders.txt", encoding="utf-8") as f:
    header = f.readline().strip().split(";")

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
os.makedirs("cities", exist_ok=True)

by_city = {}
for o in orders_all:
    by_city.setdefault(o["city"], []).append(o)

for city, city_orders in by_city.items():
    with open(f"cities/{city}.txt", "w", encoding="utf-8") as f:
        f.write(";".join(header) + "\n")
        for o in city_orders:
            values = [str(o[col]) for col in header]
            f.write(";".join(values) + "\n")

city_files = sorted(os.listdir("cities"))
order_lines = 0
for name in city_files:
    with open(f"cities/{name}", encoding="utf-8") as f:
        order_lines += len(f.readlines()) - 1    # тақырып жолын санамаймыз

print("Файлдар:", city_files, len(city_files))                        # 4
print("Тапсырыс жолдары:", order_lines, order_lines == len(orders_all))  # 12 True
