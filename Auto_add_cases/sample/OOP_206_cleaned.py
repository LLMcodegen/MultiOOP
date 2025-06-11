
class JS:
    def __init__(self, nums):
        self.nums = nums
    def __private_Judgment_segmentation(self):
        freq = {}
        subseq = {}
        for num in self.nums:
            freq[num] = freq.get(num, 0) + 1
        for num in self.nums:
            if freq[num] == 0:
                continue
            if subseq.get(num - 1, 0) > 0:
                subseq[num - 1] -= 1
                subseq[num] = subseq.get(num, 0) + 1
            elif freq.get(num + 1, 0) > 0 and freq.get(num + 2, 0) > 0:
                freq[num + 1] -= 1
                freq[num + 2] -= 1
                subseq[num + 2] = subseq.get(num + 2, 0) + 1
            else:
                return False
            freq[num] -= 1
        return True
    def public_Judgment_segmentation(self):
        return self.__private_Judgment_segmentation()

#--------------:
print(JS([1, 1, 2, 2, 3, 3]).public_Judgment_segmentation() == True)
print(JS([1, 2, 3, 3, 4, 6]).public_Judgment_segmentation() == False)
print(JS([1, 1, 2, 3, 4, 5]).public_Judgment_segmentation() == False)
