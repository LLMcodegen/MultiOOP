class FTA:
    def Find_the_array(self, target, nums):
        n = len(nums)
        min_length = float('inf')
        current_sum = 0
        left = 0
        for right in range(n):
            current_sum += nums[right]
            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1
        return min_length if min_length != float('inf') else 0
#--------------:
print(FTA().Find_the_array(21, [1, 2, 3, 4, 5, 6, 7, 8]) == 3)
print(FTA().Find_the_array(20, [5, 1, 1, 9, 6, 8]) == 3)
print(FTA().Find_the_array(50, [1, 2, 3, 10, 25]) == 0)
