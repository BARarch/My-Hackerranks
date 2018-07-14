def swap_case(s):
    return "".join([c.upper() if c.islower() else c.lower() if c.isupper() else c for c in s])
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
