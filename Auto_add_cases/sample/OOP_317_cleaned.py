
class CAY:
    def __init__(self, nums):
        self.nums = nums
class SN_CAY(CAY):
    def __init__(self, nums):
        super().__init__(nums)
    def Circular_array(self):
        n = len(self.nums)
        def kadane(arr):
            max_current = max_global = arr[0]
            for i in range(1, len(arr)):
                max_current = max(arr[i], max_current + arr[i])
                if max_current > max_global:
                    max_global = max_current
            return max_global
        max_normal = kadane(self.nums)
        total_sum = sum(self.nums)
        inverted_nums = [-x for x in self.nums]
        max_circular = total_sum + kadane(inverted_nums)
        return max(max_normal, max_circular)

#--------------:
print(SN_CAY([8, -1, 3, 4]).Circular_array() == 15)
print(SN_CAY([-4, 5, 1, 0]).Circular_array() == 6)
print(SN_CAY([2, 3, -2, 4]).Circular_array() == 9)
