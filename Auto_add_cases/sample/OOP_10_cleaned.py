class TSOTN:
    def sum_three_numbers(self, nums, target):
        if len(nums) < 3:
            raise ValueError("The input array must contain at least three elements.")
        nums.sort()
        closest_sum = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]  
                if current_sum == target:
                    return current_sum
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
        return closest_sum
#--------------:
print(TSOTN().sum_three_numbers([1, 2, 5, 10, 11], 12) == 13)
print(TSOTN().sum_three_numbers([-1, 2, 1, -4], 1) == 2)
print(TSOTN().sum_three_numbers([0, 0, 0], 1) == 0)
