import calendar

day = list(map(int, input().split(' ')))

print(calendar.day_name[calendar.weekday(day[2], day[0], day[1])].upper())
