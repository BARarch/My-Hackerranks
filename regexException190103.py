import re 

def test_regex(reg):
    try:
        a = re.compile(r'{}'.format(reg))
    except:
        return False
    else:
        return True

if __name__ == "__main__":
    N = int(input().rstrip())
    
    for _ in range(N):
        print(test_regex(input().rstrip()))
