
class FUP:
    def __init__(self, n: int):
        self.n = n
class SN_FUP(FUP):
    def __init__(self, n: int, k: int, target: int):
        super().__init__(n)
        self.k = k
        self.target = target
    def face_up(self) -> int:
        dp = [[0] * (self.target + 1) for _ in range(self.n + 1)]
        dp[0][0] = 1
        for i in range(1, self.n + 1):
            for j in range(1, self.target + 1):
                for face in range(1, self.k + 1):
                    if j - face >= 0:
                        dp[i][j] += dp[i - 1][j - face]
        return dp[self.n][self.target] % (10**9 + 7)

#--------------:
print(SN_FUP(2, 4, 5).face_up() == 4)
print(SN_FUP(3, 6, 8).face_up() == 21)
print(SN_FUP(4, 6, 10).face_up() == 80)
