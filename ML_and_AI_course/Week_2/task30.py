# Тапсырма 30. Нәтижелерді жинау

import os
import shutil

# ----- Тапсырманың шешімі -----
# Алдымен 20, 26, 27, 28 және 29-тапсырмалар іске қосылған болуы керек
needed = ["summary.txt", "category_report.csv", "customers.json", "report.txt", "cities"]
missing = [name for name in needed if not os.path.exists(name)]
if missing:
    raise SystemExit(f"Бұл файлдар әлі жоқ: {missing}. Алдымен 20, 26–29 тапсырмаларды іске қос.")

os.makedirs("results", exist_ok=True)

for name in ["summary.txt", "category_report.csv", "customers.json", "report.txt"]:
    shutil.copy(name, "results")

if os.path.exists("results/cities"):          # қайта іске қосқанда copytree қате бермес үшін
    shutil.rmtree("results/cities")
shutil.copytree("cities", "results/cities")

for root, dirs, files in os.walk("results"):
    for name in files:
        file_path = os.path.join(root, name)
        print(f"{file_path:<35} {os.path.getsize(file_path):>6} байт")

archive = shutil.make_archive("homework_results", "zip", "results")
print("Мұрағат жасалды:", archive)
# Colab-тағы files.download() PyCharm-да жоқ: zip файлы жоба бумасында тұр.
