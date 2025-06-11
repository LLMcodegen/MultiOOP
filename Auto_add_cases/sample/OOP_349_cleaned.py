
import math

class NOG:
    def __init__(self, points):
        self.points = points
class SN_NOG(NOG):
    def __init__(self, points, k):
        super().__init__(points)
        self.k = k
    def Nearest_origin(self):
        distances = [(math.sqrt(x**2 + y**2), [x, y]) for x, y in self.points]
        sorted_distances = sorted(distances, key=lambda x: x[0])
        closest_points = [point for _, point in sorted_distances[:self.k]]
        return closest_points

#--------------:
print(SN_NOG([[1,1],[2,2],[3,3],[4,4]], 2).Nearest_origin() == [[1,1],[2,2]])
print(SN_NOG([[1,1],[2,2],[3,3],[4,4]], 3).Nearest_origin() == [[1,1],[2,2],[3,3]])
print(SN_NOG([[1,1],[2,2],[3,3],[4,4]], 4).Nearest_origin() == [[1,1],[2,2],[3,3],[4,4]])
