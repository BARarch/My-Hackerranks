def centuryFromYear(year):
    if len(str(year)) < 4:
        year = '0' * (4 - (len(str(year)) % 4)) + str(year)
    else:
        year = str(year)
    if int(year[2:]) > 0:
        incr = 1   
    else:
        incr = 0
    
    return int(year[:2]) + incr
