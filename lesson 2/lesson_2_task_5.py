def month_to_season(n = int(input("введите номер месяца: "))):
    if n == 1 or n == 2 or n == 12: print("Зима")
    elif n == 3 or n == 4 or n == 5: print("Весна")
    elif n == 6 or n == 7 or n == 8: print("Лето")
    else: print ("none")

month_to_season()