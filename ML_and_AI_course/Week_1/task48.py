def average(scores):
    return sum(scores) / len(scores)

def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "F"

def best_student(journal):
    return max(journal, key=lambda name: average(journal[name]))

journal = {"Aigerim": [85, 92, 78], "Nurlan": [65, 70, 58],
           "Dana": [95, 98, 91], "Arman": [45, 52, 40]}

print(f"{'Аты':<10}{'Орташа':>8}{'Баға':>6}")
print("-" * 24)
for name, scores in journal.items():
    avg = average(scores)
    print(f"{name:<10}{avg:>8.2f}{get_grade(avg):>6}")

print("\nҮздік студент:", best_student(journal))