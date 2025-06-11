class GME:
    def __init__(self):
        pass
    @staticmethod
    def get_most_elements(nums):
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate
#--------------:
print(GME().get_most_elements([7, 8, 7, 7, 8, 7]) == 7)
print(GME().get_most_elements([6, 6, 6, 7, 8]) == 6)
print(GME().get_most_elements([4, 4, 4, 5, 5, 4]) == 4)
