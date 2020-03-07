def phoneCall(min1, min2_10, min11, s):
    mins = 0

    if s >= min1:
        s -= min1
        mins += 1
        
        while s >= min2_10 and mins >= 1 and mins < 10:
            s -= min2_10
            mins += 1

        while s >= min11 and mins >= 10:
            s -= min11
            mins += 1

        return mins

    else:
        return 0

