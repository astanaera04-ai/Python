
from orders_data import reset_orders

reset_orders()

with open("orders.txt", encoding="utf-8") as f:
    lines = [line.strip() for line in f]
header = lines[0].split(";")
data_lines = lines[1:]

fields = data_lines[0].split(";")
print(fields)

customer = fields[2]
product = fields[5]
price = int(fields[6])
quantity = int(fields[7])

amount = price * quantity
print(f"{customer}: {product}, {quantity} дана, сомасы {amount} теңге")
