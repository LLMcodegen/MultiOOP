class JI:
    def Judgment_Index(self, nums, k):
        index_map = {}
        for i, num in enumerate(nums):
            if num in index_map and i - index_map[num] <= k:
                return True
            index_map[num] = i
        return False
#--------------:
print(JI().Judgment_Index([2, 3, 4, 5, 6, 2], 5) == True)
print(JI().Judgment_Index([1, 2, 3, 4, 5], 1) == False)
print(JI().Judgment_Index([12, 15, 12, 20], 3) == True)
