# Тапсырма 3. Бір жолды бөліп алу

from orders_data import reset_orders

# orders.txt бастапқы 10 тапсырыспен қайта жазылады
reset_orders()

# ----- Алдыңғы тапсырмалардан керек деректер -----
with open("orders.txt", encoding="utf-8") as f:
    lines = [line.strip() for line in f]
header = lines[0].split(";")
data_lines = lines[1:]

# ----- Тапсырманың шешімі -----
fields = data_lines[0].split(";")
print(fields)

customer = fields[2]
product = fields[5]
price = int(fields[6])
quantity = int(fields[7])

amount = price * quantity
print(f"{customer}: {product}, {quantity} дана, сомасы {amount} теңге")
