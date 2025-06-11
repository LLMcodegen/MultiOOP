class FTM:
    def find_the_median(self, nums1, nums2):
        combined = sorted(nums1 + nums2)
        n = len(combined)
        if n % 2 == 1:
            return combined[n // 2]
        else:
            return (combined[n // 2 - 1] + combined[n // 2]) / 2
print(FTM().find_the_median([1, 2, 3], [4, 5, 6]) == 3.5)
print(FTM().find_the_median([1, 3, 8], [7, 9, 10]) == 7.5)
