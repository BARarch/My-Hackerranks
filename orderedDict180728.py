from collections import OrderedDict

def price(string):
    return int(string.split(' ')[-1])

def name(string):
    return ' '.join(string.split(' ')[:-1])

sales = OrderedDict()
N = int(input())

for _ in range(N):
    receipt = input()
    product = name(receipt)
    sold = price(receipt)
    if product in sales:
        sales[product] += sold        
    else:
        sales[product] = sold
        
for product in sales:
    print('{} {}'.format(product, sales[product]))
