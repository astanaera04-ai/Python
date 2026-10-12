SHOWS = [
"Avatar: the last airbender",
"Ben 10",
"Arthur",
"Spongebob Squarepants",
"Phineas and ferb",
"Kim possible",
"Jimmy Neutron",
"the Proud family"
]
def main():
    cleaned_shows = []
    for show in SHOWS:
        cleaned_shows.append(show.strip().title())
    print(', '.join(cleaned_shows))
main()

#String Slicing
def main():
    phone = "+1 617-495-1000"
    print(phone [8:])
main()