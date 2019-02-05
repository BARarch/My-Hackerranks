import string

def fun(s):
    atLoc = s.find('@')
    if atLoc == -1 or atLoc == 0:
        return False
    dotLoc = s.find('.')
    if dotLoc == -1:
        return False

    for ch in s[:atLoc]:
        if ch not in string.ascii_letters + '1234567890_-':
            return False

    for ch in s[atLoc + 1:dotLoc]:
        if ch not in string.ascii_letters + '1234567890':
            return False

    if len(s[dotLoc+1:]) > 3:
        return False

    return True


    
    # return True if s is a valid email, else return False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
