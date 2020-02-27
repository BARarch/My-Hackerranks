def addBorder(picture):
    def addMargin(string):
        return "*" + string + "*"

    finalWidth = len(picture[0]) + 2
    return ["*" * finalWidth, ] + list(map(addMargin, picture)) + ["*" * finalWidth, ]
