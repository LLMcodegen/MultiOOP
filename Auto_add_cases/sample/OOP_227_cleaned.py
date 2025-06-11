
class BL:
    def __init__(self, nums1, nums2):
        self.nums1 = nums1
        self.nums2 = nums2
    def __private_BLongest_length(self):
        m, n = len(self.nums1), len(self.nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        max_length = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if self.nums1[i - 1] == self.nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_length = max(max_length, dp[i][j])
        return max_length
    def public_BLongest_length(self):
        return self.__private_BLongest_length()

#--------------:
print(BL([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]).public_BLongest_length() == 0)
print(BL([1, 2, 3, 4, 5], [1, 2, 3, 4, 6]).public_BLongest_length() == 4)
print(BL([1, 2, 3, 4, 5], [1, 2, 3, 4, 6, 5]).public_BLongest_length() == 4)
