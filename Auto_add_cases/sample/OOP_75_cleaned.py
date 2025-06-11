class CTMA:
    def matrix_area(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        area1 = (ax2 - ax1) * (ay2 - ay1)
        area2 = (bx2 - bx1) * (by2 - by1)
        overlap_width = max(0, min(ax2, bx2) - max(ax1, bx1))
        overlap_height = max(0, min(ay2, by2) - max(ay1, by1))
        overlap_area = overlap_width * overlap_height
        return area1 + area2 - overlap_area
#--------------:
print(CTMA().matrix_area(-1, -1, 3, 3, -2, -2, 2, 2) == 23)
print(CTMA().matrix_area(1, 1, 5, 5, 2, 2, 6, 6) == 23)
print(CTMA().matrix_area(-2, -2, 2, 2, -3, -3, 1, 1) == 23)
