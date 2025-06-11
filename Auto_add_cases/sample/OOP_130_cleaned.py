
class RQU:
    def __init__(self, people):
        self.people = people
    def __private_Rank_queue(self):
        self.people.sort(key=lambda x: (-x[0], x[1]))
        result = []
        for person in self.people:
            result.insert(person[1], person)
        return result
    def public_Rank_queue(self):
        return self.__private_Rank_queue()

#--------------:
print(RQU([[5, 1], [6, 0], [5, 0], [7, 0]]).public_Rank_queue() == [[5, 0], [5, 1], [6, 0], [7, 0]])
print(RQU([[4, 2], [4, 1], [4, 0]]).public_Rank_queue() == [[4, 0], [4, 1], [4, 2]])
print(RQU([[5, 0], [7, 0], [6, 1], [5, 1]]).public_Rank_queue() == [[5, 0], [5, 1], [7, 0], [6, 1]])
