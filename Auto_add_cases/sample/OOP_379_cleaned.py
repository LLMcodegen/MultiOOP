
class MCT:
    def __init__(self, nums1):
        self.nums1 = nums1
class SN_MCT(MCT):
    def __init__(self, nums1, nums2):
        super().__init__(nums1)
        self.nums2 = nums2
    def max_connections(self):
        m, n = len(self.nums1), len(self.nums2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if self.nums1[i] == self.nums2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return dp[m][n]

#--------------:
print(SN_MCT([1, 2, 3], [4, 5, 6]).max_connections() == 0)
print(SN_MCT([1, 2, 3, 4], [4, 3, 2, 1]).max_connections() == 1)
print(SN_MCT([1, 2, 3, 4], [1, 2, 3, 4]).max_connections() == 4)
