year = int(input())
while(year > 0):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("кібісе жыл")
    else:
        print("кібісе жыл емес")
    year = int(input())
