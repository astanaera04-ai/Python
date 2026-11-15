# Тапсырма 16. Каталогпен салыстыру

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
catalog = {"Mouse", "Keyboard", "Headphones", "Laptop", "Python Book",
           "Novel", "Dictionary", "Notebook", "Pen", "Backpack"}

sold = {o["product"] for o in orders_dicts}
not_sold = catalog - sold

print("Сатылған тауарлар:", sorted(sold))
print("Сатылмаған тауарлар:", sorted(not_sold))              # Dictionary, Laptop
print("Барлығы каталогта бар ма:", sold.issubset(catalog))   # True
