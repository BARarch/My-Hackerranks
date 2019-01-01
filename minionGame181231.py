
def minion_game(string):
    # your code goes here
    l = len(string)
    n = 0
    StuartScore = 0
    KevinScore = 0
    vowels = 'AEIOU'

    for s in string:
        if s in vowels:
            ## Kevin's Words Start With Vowels
            KevinScore += l - n 
        else:
            StuartScore += l - n
        n += 1

    if KevinScore == StuartScore:
        print('Draw')
    elif KevinScore > StuartScore:
        print('Kevin {}'.format(str(KevinScore)))
    else:
        print('Stuart {}'.format(str(StuartScore)))

if __name__ == '__main__':
    s = input()
    minion_game(s)
