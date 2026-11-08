def process(balance, operation):
    action, amount = operation
    if action == "deposit":
        balance += amount
    elif action == "withdraw":
        if amount > balance:
            print(f"Ескерту: қаражат жеткіліксіз ({amount} шешу мүмкін емес, баланс: {balance})")
        else:
            balance -= amount
    return balance

balance = 10000
operations = [("deposit", 5000), ("withdraw", 3000), ("withdraw", 15000),
              ("deposit", 2000), ("withdraw", 4000)]

for op in operations:
    balance = process(balance, op)

print("Соңғы баланс:", balance)