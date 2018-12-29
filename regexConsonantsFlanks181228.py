import re

repeatingVowels = '([aeiouAEIOU]){2,}'
consonantsPattern = '[^W\_\-\+ aeiouAEIOU]'
betweenConsonats = re.compile('(?<={})({})(?={})'.format(consonantsPattern, repeatingVowels, consonantsPattern))

ranOnce = False

for m in betweenConsonats.findall(input().rstrip()):
    print(m[0])
    ranOnce = True

if not ranOnce:
    print(-1)
