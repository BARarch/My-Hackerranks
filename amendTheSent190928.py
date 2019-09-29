def amendTheSentence(s):
    end = 0
    start = 0
    res = []
    while end < len(s):
        if s[end].isupper():
            res.append(s[start:end].lower())
            start = end
        end += 1
        
    res.append(s[start:end].lower())
    return " ".join(res).strip()
