import re 

s = input().rstrip()
k = input().rstrip()

p = re.compile('(?={})'.format(k))

ran = False
for m in p.finditer(s):
    res = (m.start(), m.start() + len(k) - 1)
    print(res)
    ran = True

if not ran:
    print((-1, -1))
