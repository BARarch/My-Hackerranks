def arrayReplace(inputArray, elemToReplace, substitutionElem):
    def replace(imp):
        if imp == elemToReplace:
            return substitutionElem
        else:
            return imp
    return list(map(replace, inputArray))

