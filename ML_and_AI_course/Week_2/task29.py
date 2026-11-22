from orders_data import reset_orders

reset_orders(with_new_orders=True)

catalog = {"Mouse", "Keyboard", "Headphones", "Laptop", "Python Book",
           "Novel", "Dictionary", "Notebook", "Pen", "Backpack"}

def safe_load(path):
    good = []
    bad = []
    with open(path, encoding="utf-8") as f:
        columns = f.readline().strip().split(";")
        for number, line in enumerate(f, start=2):
            line = line.strip()
            if not line:
                continue
            values = line.split(";")
            try:
                values[6] = int(values[6])
                values[7] = int(values[7])
            except ValueError:
                bad.append((number, line))
                continue
            d = dict(zip(columns, values))
            d["amount"] = d["price"] * d["quantity"]
            good.append(d)
    return good, bad

def customer_stats(orders):
    stats = {}
    for o in orders:
        info = stats.setdefault(o["customer"], {"orders": 0, "total": 0, "average": 0, "cities": set()})
        info["orders"] += 1
        info["total"] += o["amount"]
        info["cities"].add(o["city"])
    for info in stats.values():
        info["average"] = round(info["total"] / info["orders"], 1)
    return stats

# ----- Тапсырманың шешімі -----
def build_report(path, report_path):
    good, bad = safe_load(path)
    total = sum(o["amount"] for o in good)
    dates = [o["date"] for o in good]

    cs = customer_stats(good)
    top_customers = sorted(cs.items(), key=lambda item: item[1]["total"], reverse=True)[:3]

    cat_revenue = {}
    for o in good:
        cat_revenue[o["category"]] = cat_revenue.get(o["category"], 0) + o["amount"]

    not_sold_items = catalog - {o["product"] for o in good}

    with open(report_path, "w", encoding="utf-8") as f:
        f.write("ИНТЕРНЕТ-ДҮКЕН ТАПСЫРЫСТАРЫ БОЙЫНША ЕСЕП\n")
        f.write("=" * 40 + "\n\n")
        f.write(f"Талдау мерзімі: {min(dates)} – {max(dates)}\n")
        f.write(f"Дұрыс жолдар: {len(good)}\n")
        f.write(f"Қате жолдар: {len(bad)}\n")
        f.write(f"Жалпы түсім: {total} теңге\n")
        f.write(f"Орташа сома: {round(total / len(good), 1)} теңге\n\n")

        f.write("Ең көп ақша жұмсаған 3 клиент:\n")
        for i, (name, info) in enumerate(top_customers, start=1):
            f.write(f"  {i}. {name:<8} {info['total']:>7} теңге\n")

        f.write("\nСанаттардың түсімдегі үлесі:\n")
        for cat, rev in sorted(cat_revenue.items(), key=lambda item: item[1], reverse=True):
            f.write(f"  {cat:<12} {rev:>7}  {rev / total * 100:.1f}%\n")

        f.write("\nКаталогтағы сатылмаған тауарлар: " + ", ".join(sorted(not_sold_items)) + "\n")


build_report("orders.txt", "report.txt")

with open("report.txt", encoding="utf-8") as f:
    print(f.read())
