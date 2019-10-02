def classifyStrings(s):
    return classifyStringsHelper(s, '', '')

def classifyStringsHelper(s, consVowels, consCons):
    vowels = 'aeiou'
    for i, c in enumerate(s):
        if c == "?":
            vowelBranch = classifyStringsHelper('a' + s[i + 1:], consVowels, consCons)
            if vowelBranch == 'mixed':
                return 'mixed'
            consBranch = classifyStringsHelper('b' + s[i + 1:], consVowels, consCons)
            if consBranch == 'mixed':
                return 'mixed'
            if consBranch != vowelBranch:
                return 'mixed'
            return consBranch
        elif c in vowels:
            consCons = ''
            consVowels += c
            if len(consVowels) == 3:
                return 'bad'
        else:
            consVowels = ''
            consCons += c
            if len(consCons) == 5:
                return 'bad'
        
    return 'good'
    
    

