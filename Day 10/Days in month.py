def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    list_of_days = [31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31, 30]
    if is_leap(year) and month == 2:
        return 29
    return list_of_days[month-1]


year = int(input("What is the year ? "))
month = int(input("What is the month ? "))
days = days_in_month(year, month)
print(days)
