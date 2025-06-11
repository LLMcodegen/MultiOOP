
class GAR:
    def __init__(self, nums):
        self.nums = nums
class SN_GAR(GAR):
    def __init__(self, nums, k):
        super().__init__(nums)
        self.k = k
    def Good_array(self):
        nums = self.nums
        k = self.k
        count = 0
        n = len(nums)
        for i in range(n):
            distinct_count = 0
            seen = set()
            for j in range(i, n):
                if nums[j] not in seen:
                    distinct_count += 1
                    seen.add(nums[j])
                if distinct_count == k:
                    count += 1
                elif distinct_count > k:
                    break
        return count

#--------------:
print(SN_GAR([1, 2, 1, 3, 4], 5).Good_array() == 0)
print(SN_GAR([1, 2, 1, 3, 4], 0).Good_array() == 0)
print(SN_GAR([1, 1, 1, 1, 1], 1).Good_array() == 15)
