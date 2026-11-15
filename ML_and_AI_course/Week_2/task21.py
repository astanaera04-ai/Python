# Тапсырма 21. Файлды оқитын функция

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
def load_orders(path):
    """Файлды оқып, тапсырыстарды сөздіктер тізімі ретінде қайтарады."""
    result = []
    with open(path, encoding="utf-8") as f:
        columns = f.readline().strip().split(";")
        for line in f:
            line = line.strip()
            if not line:                 # бос жолдарды өткізіп жіберу
                continue
            values = line.split(";")
            values[6] = int(values[6])
            values[7] = int(values[7])
            d = dict(zip(columns, values))
            d["amount"] = d["price"] * d["quantity"]
            result.append(d)
    return result


loaded = load_orders("orders.txt")
print(len(loaded))
print(loaded == orders_dicts)         # True
