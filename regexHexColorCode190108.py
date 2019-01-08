import re
codePattern = re.compile(r'(#([\dA-Fa-f]{6}|[\dA-Fa-f]{3}))[^\w\d]')
valuePattern = re.compile(r':.*?;')

if __name__ == "__main__":
    N = int(input().rstrip())
    for _ in range(N):
        for value in valuePattern.findall(input().rstrip()):
            for code in codePattern.findall(value):
                print(code[0])
