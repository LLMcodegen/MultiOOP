
class BS:
    def __init__(self, prices, fee):
        self.prices = prices
        self.fee = fee
    def _private_buy_share(self):
        n = len(self.prices)
        if n == 0:
            return 0
        cash = [0] * n
        hold = [0] * n
        hold[0] = -self.prices[0]
        for i in range(1, n):
            cash[i] = max(cash[i - 1], hold[i - 1] + self.prices[i] - self.fee)
            hold[i] = max(hold[i - 1], cash[i - 1] - self.prices[i])
        return cash[-1]
    def public_buy_share(self):
        return self._private_buy_share()

#--------------:
print(BS([7, 6, 4, 3, 1], 1).public_buy_share() == 0)
print(BS([1, 3, 7, 5, 10, 3], 3).public_buy_share() == 6)
print(BS([1, 4, 6, 2, 8, 3, 10], 2).public_buy_share() == 12)
