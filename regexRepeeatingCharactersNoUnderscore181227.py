import re

if __name__ == "__main__":
    pattern = re.compile(r'([^W\_])\1+')
    groups = pattern.findall(input().rstrip())
    if groups:
        print(groups[0])
    else:
        print(-1)
