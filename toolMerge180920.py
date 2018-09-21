def merge_the_tools(string, k):
    # your code goes here
    for start in range(0, len(string), k):
        res = ''
        for u in string[start:start + k]:
            if u not in res:
                res += u
        print(res)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
