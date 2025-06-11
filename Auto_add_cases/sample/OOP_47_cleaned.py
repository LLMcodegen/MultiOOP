class ITETAO:
    def Appeared_Once(self, nums):
        unique_element = 0
        for num in nums:
            unique_element ^= num
        return unique_element
#--------------:
print(ITETAO().Appeared_Once([8, 9, 8, 7, 9]) == 7)
print(ITETAO().Appeared_Once([13, 19, 13, 19, 21]) == 21)
print(ITETAO().Appeared_Once([5, 6, 6]) == 5)
