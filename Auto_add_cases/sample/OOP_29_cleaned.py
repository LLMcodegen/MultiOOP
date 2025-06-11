class MMJL:
    def maximum_jump_length(self, nums):
        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
            if max_reach >= len(nums) - 1:
                return True
        return False
#--------------:
print(MMJL().maximum_jump_length([10, 0, 0, 0]) == True)
print(MMJL().maximum_jump_length([1, 1, 1, 1, 1]) == True)
print(MMJL().maximum_jump_length([2, 5, 0, 0, 1, 0, 1]) == True)
