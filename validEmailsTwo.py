#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 201102

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
def fun(s):
    # return True if s is a valid email, else return False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
