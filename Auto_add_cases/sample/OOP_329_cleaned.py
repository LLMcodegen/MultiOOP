
class MAR:
    def __init__(self, drop):
        self.drop = drop
class SN_MAR(MAR):
    def Minimum_Area(self):
        points = self.drop
        point_set = set(map(tuple, points))
        min_area = float('inf')
        n = len(points)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                if x1 != x2 and y1 != y2:
                    if (x1, y2) in point_set and (x2, y1) in point_set:
                        area = abs(x1 - x2) * abs(y1 - y2)
                        min_area = min(min_area, area)
        return min_area if min_area != float('inf') else 0

#--------------:
print(SN_MAR([[0,0],[0,4],[4,0],[4,4],[2,2]]).Minimum_Area() == 16)
print(SN_MAR([[1,1],[1,5],[5,1],[5,5],[3,3]]).Minimum_Area() == 16)
print(SN_MAR([[0,0],[0,5],[5,0],[5,5],[2,2],[3,3]]).Minimum_Area() == 25)
