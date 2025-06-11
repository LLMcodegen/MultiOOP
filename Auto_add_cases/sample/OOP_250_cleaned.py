
class FR:
    def __init__(self, answers):
        self.answers = answers
    def __private_Forest_Rabbit(self):
        from collections import Counter
        answer_count = Counter(self.answers)
        min_rabbits = 0
        for answer, count in answer_count.items():
            group_size = answer + 1
            complete_groups = (count + group_size - 1) // group_size
            min_rabbits += complete_groups * group_size
        return min_rabbits
    def public_Forest_Rabbit(self):
        return self.__private_Forest_Rabbit()

#--------------:
print(FR([1, 1, 1, 1]).public_Forest_Rabbit() == 4)
print(FR([2, 2, 2, 2]).public_Forest_Rabbit() == 6)
print(FR([3, 3, 3, 3]).public_Forest_Rabbit() == 4)
