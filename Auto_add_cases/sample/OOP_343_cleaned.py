
from itertools import combinations, permutations
import math

class ARE:
    def __init__(self, drop):
        self.drop = drop
class SN_ARE(ARE):
    def Any_rectangle(self):
        min_area = float('inf')
        points = self.drop
        n = len(points)
        point_list = [tuple(p) for p in points]
        point_set = set(point_list)
        for quad in combinations(point_list, 4):
            for perm in permutations(quad):
                A, B, C, D = perm
                AB = (B[0]-A[0], B[1]-A[1])
                BC = (C[0]-B[0], C[1]-B[1])
                CD = (D[0]-C[0], D[1]-C[1])
                DA = (A[0]-D[0], A[1]-D[1])
                if (AB[0]*BC[0] + AB[1]*BC[1] != 0):
                    continue
                if (BC[0]*CD[0] + BC[1]*CD[1] != 0):
                    continue
                if (CD[0]*DA[0] + CD[1]*DA[1] != 0):
                    continue
                if (DA[0]*AB[0] + DA[1]*AB[1] != 0):
                    continue
                len_AB2 = AB[0]**2 + AB[1]**2
                len_BC2 = BC[0]**2 + BC[1]**2
                len_CD2 = CD[0]**2 + CD[1]**2
                len_DA2 = DA[0]**2 + DA[1]**2
                if len_AB2 != len_CD2:
                    continue
                if len_BC2 != len_DA2:
                    continue
                area = math.sqrt(len_AB2) * math.sqrt(len_BC2)
                if area < min_area:
                    min_area = area
        if min_area == float('inf'):
            return 0
        else:
            return round(min_area + 1e-8, 5)

#--------------:
print(SN_ARE([[0,0], [1,0], [1,1], [0,1]]).Any_rectangle() == 1.0)
print(SN_ARE([[0,0], [2,0], [2,1], [0,1]]).Any_rectangle() == 2.0)
print(SN_ARE([[0,0], [2,0], [2,1], [0,1], [1,0], [1,1]]).Any_rectangle() == 1.0)