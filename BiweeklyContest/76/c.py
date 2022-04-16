class ATM(object):

    def __init__(self):
        self.bank = [0] * 5
        self.dollar = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount):
        """
        :type banknotesCount: List[int]
        :rtype: None
        """
        for i in range(5):
            self.bank[i] += banknotesCount[i]
        

    def withdraw(self, amount):
        """
        :type amount: int
        :rtype: List[int]
        """
        ret = [0] * 5
        for i in range(4, -1, -1):
            ret[i] = min(amount // self.dollar[i], self.bank[i])
            amount -= ret[i]*self.dollar[i]
        if amount == 0:
            for i in range(5):
                self.bank[i] -= ret[i]
            return ret
        else:
            return [-1]
