
import math

class FAS:
    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
    def __distance(self, point1, point2):
        return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
    def __Form_square(self):
        points = [self.p1, self.p2, self.p3, self.p4]
        distances = [self.__distance(points[i], points[j]) for i in range(4) for j in range(i + 1, 4)]
        distances.sort()
        return (distances[0] == distances[1] == distances[2] == distances[3] and distances[4] == distances[5] and distances[4] == math.sqrt(2) * distances[0])
    def public_Form_square(self):
        return self.__Form_square()

#--------------:
print(FAS([1, 1], [3, 1], [3, 3], [1, 3]).public_Form_square() == True)
print(FAS([0, 0], [1, 2], [2, 1], [1, 1]).public_Form_square() == False)
print(FAS([0, 0], [2, 0], [1, 1], [0, 2]).public_Form_square() == False)
