with open("orders.txt", encoding="utf-8") as f:
    lines = []
    for line in f:
        lines.append(line.strip())

for line in lines:
    print(line)