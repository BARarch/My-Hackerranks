#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200925

import math
import os
import random
import re
import sys
import qtimer


# Complete the function below.
@qtimer.timeit
def htmlLink(text):
    soup = BeautifulSoup(text, features="html.parser")
    links = soup.select('a')

    for link in links:
        ref = link['href'].replace("&", "&amp;")
        content = link.string
        if content:
            print(f'{ref},{str(content).strip()}')
        else:
            print(f'{ref},')
        #if link.contents:
        #    content = link.string
        #    if len(content):
        #        print(f'{ref},{content}')
        #    else:
        #        print(f'{ref},')
        #else:
        #    print(f'{ref},')


if __name__ == "__main__":
    from bs4 import BeautifulSoup
    N = int(input())
    text = "\n".join([input() for _ in range(N)])

    htmlLink(text)
