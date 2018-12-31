import re 

def and_switch(match):
    return 'and'

def or_switch(match):
    return 'or'

if __name__ == "__main__":
    N = int(input().rstrip())

    for _ in range(N):
        print(re.sub(r'(?<= )\|\|(?= )', or_switch, re.sub(r'(?<= )\&\&(?= )', and_switch, input().rstrip())))
