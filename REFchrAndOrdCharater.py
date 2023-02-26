## This is code for LeetCodes 1844 Replace All Digits with Characters

import string

if __name__ == "__main__":
    letters = string.ascii_lowercase
    s = "a1b2c3d4e"
    letterHere = True
    res = ''
    for c in s:
        if letterHere:
            a = c
        else:
            a = letters[letters.index(a) + int(c)]
        res += a
        letterHere = not letterHere 

        ## consider ord and chr
        ## chr(ord(c) + d)

    print(res)


   

