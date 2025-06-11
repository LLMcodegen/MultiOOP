
class RB:
    def __init__(self, boxes):
        self.boxes = boxes
    def __private_Remove_Box(self, boxes, memo):
        if not boxes:
            return 0
        key = tuple(boxes)
        if key in memo:
            return memo[key]
        length = len(boxes)
        max_points = 0
        i = 0
        while i < length:
            color = boxes[i]
            count = 0
            start = i
            while i < length and boxes[i] == color:
                count += 1
                i += 1
            new_boxes = boxes[:start] + boxes[start + count:]
            points = count * count + self.__private_Remove_Box(new_boxes, memo)
            max_points = max(max_points, points)
        memo[key] = max_points
        return max_points
    def public_Remove_Box(self):
        memo = {}
        return self.__private_Remove_Box(self.boxes, memo)

#--------------:
print(RB([1, 3, 2, 4, 3, 1]).public_Remove_Box() == 10)
print(RB([1, 1, 2, 2, 2, 1]).public_Remove_Box() == 18)
print(RB([4, 4, 4, 4]).public_Remove_Box() == 16)
