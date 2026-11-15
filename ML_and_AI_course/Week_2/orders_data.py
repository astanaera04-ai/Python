# Барлық тапсырма файлдарына ортақ көмекші модуль.
# Ол тапсырманың бөлігі емес: тек orders.txt файлын дұрыс күйге келтіреді.

ORIGINAL_ORDERS = """order_id;date;customer;city;category;product;price;quantity
O101;2026-10-01;Aigerim;Almaty;Electronics;Mouse;6500;2
O102;2026-10-02;Nurlan;Astana;Books;Python Book;9500;1
O103;2026-10-03;Dana;Almaty;Stationery;Notebook;900;10
O104;2026-10-05;Aigerim;Almaty;Books;Novel;4800;2
O105;2026-10-08;Arman;Shymkent;Electronics;Headphones;25000;1
O106;2026-10-10;Nurlan;Astana;Stationery;Pen;350;20
O107;2026-10-12;Dana;Astana;Electronics;Keyboard;14000;1
O108;2026-10-15;Madina;Shymkent;Books;Python Book;9500;2
O109;2026-10-18;Aigerim;Almaty;Stationery;Backpack;15500;1
O110;2026-10-20;Arman;Shymkent;Electronics;Mouse;6500;3
"""

NEW_LINES = [
    "O111;2026-10-25;Madina;Karaganda;Books;Novel;4800;3",
    "O112;2026-10-28;Nurlan;Astana;Electronics;Headphones;25000;2",
    "O113;2026-10-30;Dana;Almaty;Stationery;Pen;350;two",
]


def reset_orders(with_new_orders=False):
    """orders.txt файлын бастапқы 10 тапсырыспен қайта жазады.
    with_new_orders=True болса, 24-тапсырмада қосылатын 3 жолды да қосады."""
    with open("orders.txt", "w", encoding="utf-8") as f:
        f.write(ORIGINAL_ORDERS)
        if with_new_orders:
            for line in NEW_LINES:
                f.write(line + "\n")
