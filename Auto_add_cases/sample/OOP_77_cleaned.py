class GTAC:
    def array_count(self, nums):
        if not nums:
            return []
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0
        for num in nums:
            if candidate1 is not None and num == candidate1:
                count1 += 1
            elif candidate2 is not None and num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        result = []
        count1, count2 = 0, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
        n = len(nums)
        if count1 > n // 3:
            result.append(candidate1)
        if count2 > n // 3:
            result.append(candidate2)
        return result
#--------------:
print(GTAC().array_count([0, 0, 0, 1, 2, 2, 2]) == [0, 2])
print(GTAC().array_count([5, 5, 5, 9, 9, 9, 9]) == [5, 9])
print(GTAC().array_count([10, 10, 20, 20, 30, 30, 30]) == [30])
