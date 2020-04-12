def pagesNumberingWithInk(current, numberOfDigits):
    from itertools import count
    page = count(current)
    for pageNumber in page:
        numberOfDigits -= len(str(pageNumber))
        if numberOfDigits >= 0:
            last = pageNumber
        else:
            return last

