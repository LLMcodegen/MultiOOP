from functools import lru_cache

class SGA:
    def __init__(self, piles):
        self.piles = piles
class SN_SGA(SGA):
    def Stone_Game(self):
        n = len(self.piles)
        suffix_sums = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sums[i] = suffix_sums[i + 1] + self.piles[i]
        @lru_cache(None)
        def dfs(i, M):
            if i >= n:
                return 0
            max_stones = 0
            for X in range(1, min(2 * M, n - i) + 1):
                next_M = max(M, X)
                opponent_stones = dfs(i + X, next_M)
                alice_stones = suffix_sums[i] - opponent_stones
                max_stones = max(max_stones, alice_stones)
            return max_stones
        return dfs(0, 1)

#--------------:
print(SN_SGA([1,2,3,4,5,6,7,8,9]).Stone_Game() == 25)
print(SN_SGA([1,2,3,4,5,6,7,8,9,10]).Stone_Game() == 26)
print(SN_SGA([1,2,3,4,5,6,7,8,9,10,11]).Stone_Game() == 35)
