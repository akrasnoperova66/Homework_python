def month_to_season(month):
    if month == 12 or month <=2:
        return "Зима"
    if 2 < month <=5:
        return "Весна"
    if 5 < month <= 8:
        return "Лето"
    if 8 < month <= 11:
        return "Осень"
    

month = int(input("Введите номер месяца (1-12): "))
print(month_to_season(month))