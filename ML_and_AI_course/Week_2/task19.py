# Тапсырма 19. Клиент сатып алған тауарлар

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
customer_products = {}

for o in orders_dicts:
    customer_products.setdefault(o["customer"], []).append(o["product"])

for name, items in customer_products.items():
    print(name, "-", ", ".join(items))
