import datetime

def solution(a, b):
    day = datetime.date(2016, a, b)
    if day.weekday() == 0:
        return "MON"
    elif day.weekday() == 1:
        return "TUE"
    elif day.weekday() == 2:
        return "WED"
    elif day.weekday() == 3:
        return "THU"
    elif day.weekday() == 4:
        return "FRI"
    elif day.weekday() == 5:
        return "SAT"
    else:
        return "SUN"
