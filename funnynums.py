class ProductReg():
    def __init__(self):
        self.prods = [1, ]
        self.intts = []
        self.prod = 1
        self.validK = 0
        self.hasZero = False

    def insert(self, intt):
        self.intts.append(intt)
        if intt == 0:
            self.validK = 0
            self.prods = [1, ]
            self.hasZero = True
        else:
            self.prods.append(self.prods[-1] * intt)
            self.validK += 1

    def product(self, k):
        if k <= self.validK:
            return self.prods[-1] // self.prods[-(k + 1)]
        if self.hasZero:
            return 0
        else:
            return self.prods[-1]

    def __repr__(self):
        return str(self.intts)
