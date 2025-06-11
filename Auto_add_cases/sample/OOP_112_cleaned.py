
class DSS:
    def __init__(self, nums):
        self.nums = nums

    def __private_Divisible_subset(self):
        if not self.nums:
            return []
        self.nums.sort()
        dp = [1] * len(self.nums)
        prev = [-1] * len(self.nums)
        max_index = 0
        for i in range(1, len(self.nums)):
            for j in range(i):
                if self.nums[i] % self.nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j
                    if dp[i] > dp[max_index]:
                        max_index = i
        answer = []
        while max_index != -1:
            answer.append(self.nums[max_index])
            max_index = prev[max_index]
        return answer[::-1]
    def public_Divisible_subset(self):
        return self.__private_Divisible_subset()

#--------------:
print(DSS([1, 11, 22, 33, 66]).public_Divisible_subset() == [1, 11, 22, 66])
print(DSS([3, 5, 15]).public_Divisible_subset() == [3, 15])
print(DSS([1, 4, 16, 64]).public_Divisible_subset() == [1, 4, 16, 64])
