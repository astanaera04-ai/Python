# Тапсырма 24. Файлға жаңа тапсырыстар қосу

from orders_data import reset_orders

# orders.txt бастапқы күйге келтіріледі, сондықтан файлды қанша рет іске қоссаң да жолдар 14 болады
reset_orders()

# ----- Тапсырманың шешімі -----
new_lines = [
    "O111;2026-10-25;Madina;Karaganda;Books;Novel;4800;3",
    "O112;2026-10-28;Nurlan;Astana;Electronics;Headphones;25000;2",
    "O113;2026-10-30;Dana;Almaty;Stationery;Pen;350;two",
]

with open("orders.txt", "a", encoding="utf-8") as f:
    for line in new_lines:
        f.write(line + "\n")

with open("orders.txt", encoding="utf-8") as f:
    file_lines = [line for line in f if line.strip()]

print("Файлдағы жолдар саны:", len(file_lines))     # 14
