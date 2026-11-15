# Тапсырма 12. Тапсырыстарды сүзу

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
big_orders = [o["order_id"] for o in orders_dicts if o["amount"] > 10000]
almaty_orders = [o["order_id"] for o in orders_dicts if o["city"] == "Almaty"]

print("10 000-нан асатын:", big_orders)        # 6 тапсырыс
print("Almaty:", almaty_orders)                # 4 тапсырыс
