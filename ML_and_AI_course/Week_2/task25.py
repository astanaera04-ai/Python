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


orders_all, errors = safe_load("orders.txt")
print("Дұрыс тапсырыстар:", len(orders_all))
print("Қате жолдар:", errors)
print("Жалпы түсім:", sum(o["amount"] for o in orders_all))
