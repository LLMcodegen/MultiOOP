
class MSS:
    def __init__(self, people):
        self.people = people
class SN_MSS(MSS):
    def __init__(self, people, limit):
        super().__init__(people)
        self.limit = limit
    def Minimum_ships(self):
        self.people.sort()
        left = 0
        right = len(self.people) - 1
        boats = 0
        while left <= right:
            if left == right:
                boats += 1
                break
            if self.people[left] + self.people[right] <= self.limit:
                left += 1
                right -= 1
            else:
                right -= 1
            boats += 1
        return boats

#--------------:
print(SN_MSS([1, 2, 3, 4], 6).Minimum_ships() == 2)
print(SN_MSS([1, 2, 3, 4], 7).Minimum_ships() == 2)
print(SN_MSS([1, 2, 3, 4], 8).Minimum_ships() == 2)
