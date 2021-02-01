#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 201102

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.

import string


def fun(s):
    if '@' not in s or '.' not in s:
        return False

    user_name = s[:s.index('@')]
    if len(user_name) == 0:
        return False
    for c in user_name:
        if c not in string.digits + string.ascii_lowercase + "_" + "-":
            return False
    website_name = s[s.index('@') + 1:s.index('.')]
    if len(website_name) == 0:
        return False
    for c in website_name:
        if c not in string.digits + string.ascii_lowercase:
            return False

    extention = s[s.index('.') + 1:]
    return len(extention) <= 3

    # return True if s is a valid email, else return False


@qtimer.timeit
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
