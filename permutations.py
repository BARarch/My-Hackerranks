from functools import reduce
from operator import add


def perms(s):
    def perms_help(prime):
        res = []
        for c in filter(lambda x: x not in prime, s):
            res.append(prime + c)
        return res + reduce(add, [perms_help(r) for r in res], [])

    return perms_help('')


if __name__ == "__main__":
    print(perms('aba'))