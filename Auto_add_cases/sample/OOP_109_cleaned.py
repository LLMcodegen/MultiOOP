
class RDL:
    def __init__(self, envelopes):
        self.envelopes = envelopes

    def __private_Russian_dolls(self):
        if not self.envelopes:
            return 0
        self.envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = [0] * len(self.envelopes)
        length = 0
        for _, h in self.envelopes:
            left, right = 0, length
            while left < right:
                mid = (left + right) // 2
                if dp[mid] < h:
                    left = mid + 1
                else:
                    right = mid
            dp[left] = h
            if left == length:
                length += 1
        return length
    def public_Russian_dolls(self):
        return self.__private_Russian_dolls()

#--------------:
print(RDL([[3, 2], [4, 5], [5, 4], [6, 8], [7, 6]]).public_Russian_dolls() == 3)
print(RDL([[1, 3], [3, 5], [2, 4], [5, 7]]).public_Russian_dolls() == 4)
print(RDL([[10, 8], [12, 10], [8, 7], [9, 9]]).public_Russian_dolls() == 3)
