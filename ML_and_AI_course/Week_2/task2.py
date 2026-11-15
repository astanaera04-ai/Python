with open("orders.txt", encoding="utf-8") as f:
    lines = []
    for line in f:
        lines.append(line.strip())


header = lines[0].split(";")
data_lines = lines[1:]

for number, column in enumerate(header, start=1):
    print(number, column)

print("Тапсырыстар саны:", len(data_lines))
