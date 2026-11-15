# Тапсырма 7. Тауарлар тізімін сұрыптау

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

# ----- Тапсырманың шешімі -----
products = []
for order in orders:
    products.append(order[5])

products.sort()
print("Сұрыпталған:", products)

products.append("Laptop")
print("Қосылғаннан кейін:", products)

products.remove("Laptop")
print("Өшірілгеннен кейін:", products)
