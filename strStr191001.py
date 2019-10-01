def strstr(s, x):
    check = 0
    if x not in s:
        return -1
    while check + len(x) <= len(s):
        if s[check:check + len(x)] == x:
            return check
        check += 1
