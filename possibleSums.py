#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 190911
import os
from cs_utils import *

def possibleSums(coins, quantity):
    sums = {0: '',}
    for coin, count in zip(coins, quantity):
        #print(len(sums))
        new = {}
        for n in range(1, count + 1):
            for summ in sums:
                if (summ + (n * coin)) not in sums:
                    #print("summ: {}   n * coin: {}   n: {}".format(summ, n * coin, n))
                    new[summ + (n * coin)] = ''
        for summ in new:
            sums[summ] = ''

            #print(sums)

        

    return len(sums) - 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    coins = list_string_to_list(input())
    quantity = list_string_to_list(input())

    print("coins: {}".format(coins))
    print("quantity: {}".format(quantity))


    fptr.write(str(possibleSums(coins, quantity)))
    fptr.write('\n')

    fptr.close()
