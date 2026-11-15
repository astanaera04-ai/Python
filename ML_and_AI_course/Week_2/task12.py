from orders_data import reset_orders

reset_orders()

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

big_orders = [o["order_id"] for o in orders_dicts if o["amount"] > 10000]
almaty_orders = [o["order_id"] for o in orders_dicts if o["city"] == "Almaty"]

print("10 000-нан асатын:", big_orders)
print("Almaty:", almaty_orders)
