class ERTTR:
    def element_rotates(self, nums, k):
        n = len(nums)
        k = k % n
        nums[:] = nums[-k:] + nums[:-k]
        return nums
#--------------:
print(ERTTR().element_rotates([100, 200, 300], 2) == [200, 300, 100])
print(ERTTR().element_rotates([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4, 5])
print(ERTTR().element_rotates([0, 0, 0], 3) == [0, 0, 0])
