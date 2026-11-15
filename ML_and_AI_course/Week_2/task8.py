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

first = tuple(orders[0])
print(first)

order_id, date, customer, city, category, product, price, quantity = first
print(order_id, date, customer)

try:
    first[6] = 1000
except TypeError as error:
    print("Қате:", error)
