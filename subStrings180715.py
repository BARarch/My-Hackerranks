def count_substring(string, sub_string):
    nMatches = 0
    for start in range(len(string) - len(sub_string) + 1):
        if string[start : start + len(sub_string)] == sub_string:
            nMatches += 1
    return nMatches

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
