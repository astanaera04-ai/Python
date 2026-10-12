def get_words(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()

    words = []
    for word in text.split():
        word = word.strip(".,!?;:\"'()-")  # тыныс белгілерін алып тастау
        if word:  # бос жол болмаса ғана
            words.append(word)
    return words

def save_counts(counts):
    with open("counts.txt", "w", encoding="utf-8") as f:
        for word, count in counts.items():
            f.write(f"{word}: {count}\n")
def main():

    words = get_words("address.txt")
    lowercase_words = [word.lower() for word in words if len(word) > 4]

    counts = {word: words.count(word) for word in lowercase_words}
    save_counts(counts)

main()