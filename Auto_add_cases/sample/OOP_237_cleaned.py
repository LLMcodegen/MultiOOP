
class IC:
    def __init__(self, intervals):
        self.intervals = intervals
    def __private_Include_Collection(self):
        self.intervals.sort(key=lambda x: x[1])
        nums = []
        last_point = -1
        second_last_point = -1
        for interval in self.intervals:
            start, end = interval
            if start > last_point:
                second_last_point = end - 1
                last_point = end
                nums.extend([second_last_point, last_point])
            elif start > second_last_point:
                second_last_point = last_point
                last_point = end
                nums.append(last_point)
        return len(nums)
    def public_Include_Collection(self):
        return self.__private_Include_Collection()

#--------------:
print(IC([[1, 3], [2, 4], [3, 5], [4, 6]]).public_Include_Collection() == 4)
print(IC([[1, 4], [2, 5], [3, 6], [4, 7]]).public_Include_Collection() == 3)
print(IC([[1, 5], [2, 6], [3, 7], [4, 8], [5, 9]]).public_Include_Collection() == 3)
