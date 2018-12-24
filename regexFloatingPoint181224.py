import re

if __name__ == "__main__":
    pattern = re.compile('^[-+]?\d*\.\d+$')
    n = int(input())
    for _ in range(n):
        print(bool(pattern.match(input().rstrip())))
