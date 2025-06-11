class FSAEP:
    def finding_positions(self, nums, target):
        def find_first(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left if left < len(nums) and nums[left] == target else -1
        def find_last(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right if right >= 0 and nums[right] == target else -1
        first_position = find_first(nums, target)
        last_position = find_last(nums, target)
        return [first_position, last_position] if first_position != -1 else [-1, -1]
#--------------:
#--------------:
print(FSAEP().finding_positions([2, 4, 4, 4, 5, 6], 4) == [1, 3])
print(FSAEP().finding_positions([5, 5, 5, 5, 5], 5) == [0, 4])
print(FSAEP().finding_positions([1, 3, 3, 3, 7], 3) == [1, 3])
