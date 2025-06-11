
class NBGG:
    def __init__(self, n):
        self.n = n
    def __private_Guessing_Game(self, start, end, memo):
        if start >= end:
            return 0
        if memo[start][end] != -1:
            return memo[start][end]
        min_cash = float('inf')
        for x in range(start, end + 1):
            cash = x + max(self.__private_Guessing_Game(start, x - 1, memo), self.__private_Guessing_Game(x + 1, end, memo))
            min_cash = min(min_cash, cash) 
        memo[start][end] = min_cash
        return min_cash
    def __private_ugly_number(self, result):
        return result
    def public_Guessing_Game(self):
        memo = [[-1] * (self.n + 1) for _ in range(self.n + 1)]
        min_cash_to_win = self.__private_Guessing_Game(1, self.n, memo)
        return self.__private_ugly_number(min_cash_to_win)

#--------------:
print(NBGG(8).public_Guessing_Game() == 12)
print(NBGG(9).public_Guessing_Game() == 14)
print(NBGG(11).public_Guessing_Game() == 18)
