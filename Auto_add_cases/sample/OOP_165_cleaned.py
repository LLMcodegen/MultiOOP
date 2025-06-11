
class IFIP:
    def __init__(self, nums):
        self.nums = nums
    def __private_Important_flipping(self):
        def merge_sort(arr, start, end):
            if start >= end:
                return 0
            mid = (start + end) // 2
            count = merge_sort(arr, start, mid) + merge_sort(arr, mid + 1, end)
            j = mid + 1
            for i in range(start, mid + 1):
                while j <= end and arr[i] > 2 * arr[j]:
                    j += 1
                count += j - (mid + 1)
            merged = []
            left, right = start, mid + 1
            while left <= mid and right <= end:
                if arr[left] <= arr[right]:
                    merged.append(arr[left])
                    left += 1
                else:
                    merged.append(arr[right])
                    right += 1
            while left <= mid:
                merged.append(arr[left])
                left += 1
            while right <= end:
                merged.append(arr[right])
                right += 1
            for i, val in enumerate(merged):
                arr[start + i] = val
            return count
        return merge_sort(self.nums, 0, len(self.nums) - 1)
    def public_Important_flipping(self):
        return self.__private_Important_flipping()

#--------------:
print(IFIP([7, 5, 3, 2]).public_Important_flipping() == 3)
print(IFIP([8, 4, 2, 1]).public_Important_flipping() == 3)
print(IFIP([2, 1, 3, 1]).public_Important_flipping() == 1)
