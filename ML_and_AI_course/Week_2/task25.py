# Тапсырма 25. Қатеге төзімді оқу

from orders_data import reset_orders

# 24-тапсырмадан кейінгі күй: бастапқы 10 тапсырыс + 3 жаңа жол
reset_orders(with_new_orders=True)

# ----- Тапсырманың шешімі -----
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
print("Дұрыс тапсырыстар:", len(orders_all))       # 12
print("Қате жолдар:", errors)                      # [(14, 'O113;...;two')]
print("Жалпы түсім:", sum(o["amount"] for o in orders_all))   # 205500
