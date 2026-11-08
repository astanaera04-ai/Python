def check_guess(secret, guess):
    if guess > secret:
        return "Ойлаған сан кішірек"
    elif guess < secret:
        return "Ойлаған сан үлкенірек"
    else:
        return "Таптыңыз!"

secret = 42
guesses = [50, 25, 37, 45, 42, 30]

for attempt, guess in enumerate(guesses, start=1):
    result = check_guess(secret, guess)
    print(f"{guess}: {result}")
    if guess == secret:
        print("Әрекеттер саны:", attempt)
        break