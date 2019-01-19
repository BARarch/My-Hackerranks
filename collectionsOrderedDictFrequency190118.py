import math
import os
import random
import re
import sys

from collections import OrderedDict

if __name__ == '__main__':
    s = sorted(input())
    a = OrderedDict([(x, []) for x in range(len(s), 0, -1)])

    last = s[0]
    count = 1
    for c in s[1:]:
        if c == last:
            count += 1
        else:
            if last:
                a[count].append(last)
                last = c
                count = 1
    if last:
        a[count].append(last)

    outs = 0
    for q in a:
        if outs < 3:
            for char in a[q]:
                if outs < 3:
                    print('{} {}'.format(char, str(q)))
                    outs += 1
                else:
                    break
        else:
            break
