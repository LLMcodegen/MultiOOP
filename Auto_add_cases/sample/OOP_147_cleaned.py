
import math
from collections import defaultdict

class EDA:
    def __init__(self, points):
        self.points = points
    def __private_Euclidean_distance(self, p1, p2):
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
    def public_Euclidean_distance(self):
        count = 0
        for i in range(len(self.points)):
            distances = defaultdict(int)
            for j in range(len(self.points)):
                if i != j:
                    distance = self.__private_Euclidean_distance(self.points[i], self.points[j])
                    distances[distance] += 1
            for d in distances.values():
                if d > 1:
                    count += d * (d - 1)
        return count

#--------------:
print(EDA([[0,0], [0,2], [3,0], [3,2]]).public_Euclidean_distance() == 0)
print(EDA([[0,0], [1,1], [0,0], [1,1], [2,2]]).public_Euclidean_distance() == 20)
print(EDA([[0,0], [1,1], [2,0], [1,-1], [0,0]]).public_Euclidean_distance() == 20)
