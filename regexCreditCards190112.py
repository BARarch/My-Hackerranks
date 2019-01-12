import re

cnPattern = re.compile(r'^((4|5|6)\d{3})\-?(\d{4})\-?(\d{4})\-?(\d{4})$')

def four_consecutive(digit):
    return re.compile(digit + r'{4}')

def digits(m):
    # get all digits and digits only from groups in match m
    return m.group(1) + m.group(3) + m.group(4) + m.group(5)

def four_of_a_kind(digits):
    for digit in digits:
        if bool(four_consecutive(digit).search(digits)):
            return True
    return False

if __name__ == '__main__':
    N = int(input().rstrip())
    for _ in range(N):
        m = cnPattern.match(input().rstrip())
        if bool(m):
            if four_of_a_kind(digits(m)):
                print('Invalid')
            else:
                print('Valid')
        else:
            print('Invalid')
