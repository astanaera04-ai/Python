header = ...       # Шешіміңізді осында жазыңыз
data_lines = ...   # Шешіміңізді осында жазыңыз

for number, column in enumerate(header, start=1):
    print(number, column)

print("Тапсырыстар саны:", len(data_lines))