import re 

uidChars = re.compile(r'^[^\W_]{10}$')
upperPattern = re.compile(r'[A-Z]')
digitPattern = re.compile(r'\d')

def validate(uidIn):
    ## Remove repeat charaters
    uid = ''.join(set(uidIn))

    ## 10 Character Length
    if (len(uidIn) != len(uid)) or (len(uid) != 10):
        return "Invalid"

    ## Contains Alphanumeric Charaters Only
    if not bool(uidChars.match(uid)):
        return "Invalid"

    ## At Least 3 Digits
    if len(digitPattern.findall(uid)) < 3:
        return "Invalid"

    ## At Least 2 UpperCase
    if len(upperPattern.findall(uid)) < 2:
        return "Invalid"

    return "Valid"
    

if __name__ == "__main__":
    for _ in range(int(input().rstrip())):
        print(validate(input().rstrip()))
