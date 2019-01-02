import re 

phoneNumPattern = re.compile(r'^(7|8|9)\d{9}$')

if __name__ == "__main__":
    N = int(input().rstrip())

    for _ in range(N):
        if phoneNumPattern.match(input().rstrip()):
            print("YES")
        else:
            print("NO")

