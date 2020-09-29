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
    soup = BeautifulSoup(text, features="lxml")
    links = soup.select('a')

    for link in links:
        ref = link['href']
        content = link.contents[0]
        print(f'{ref},{content}')


if __name__ == "__main__":
    from bs4 import BeautifulSoup
    N = int(input())
    text = "\n".join([input() for _ in range(N)])

    htmlLink(text)
