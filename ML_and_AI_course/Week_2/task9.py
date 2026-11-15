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
print(orders)
customers = [order[2] for order in orders]

unique_customers = set(customers)
print(unique_customers, len(unique_customers))

cities = set()
for order in orders:
    cities.add(order[3])

print(cities, len(cities))
