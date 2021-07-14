def newStyleFormatting(s):
    res = ""
    skipCheck = False
    for i, c in enumerate(s):
        if skipCheck:
            skipCheck = False
        elif c == "%":
            skipCheck = True
            if s[i + 1] == "%":
                res += "%"
            else:
                res += "{}"
        else:
            res += c

    return res

if __name__ == "__main__":
    print(newStyleFormatting(input()))