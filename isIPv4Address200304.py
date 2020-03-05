def circleOfNumbers(n, firstNumber):
    return (firstNumber + n // 2) % n 


def isIPv4Address(inputString):
    count = 0
    for address in inputString.split("."):
        count += 1
        if not address.isnumeric():
            return False
        
        if int(address) < 0 or int(address) > 255:
            return False

    if count == 4:
        return True
    else:
        return False

