def commonCharacterCount(s1, s2):
    commonChars = set(s1).intersection(s2)
    res = []
    for i in commonChars:
        res.append(min(s1.count(i), s2.count(i)))
    return sum(res)
    
