
class SPR:
    def __init__(self, nums):
        self.nums = nums
    def __private_Suences_patterns(self):
        n = len(self.nums)
        visited = [False] * n
        for start in range(n):
            if not visited[start]:
                direction = None
                seq = []
                index = start
                while True:
                    if visited[index]:
                        break
                    visited[index] = True
                    seq.append(index)
                    if self.nums[index] > 0:
                        if direction is None:
                            direction = True
                        elif not direction:
                            break
                    else:
                        if direction is None:
                            direction = False
                        elif direction:
                            break
                    index = (index + self.nums[index]) % n
                    if index == start:
                        if len(seq) > 1:
                            return True
                        break
        return False
    def public_Suences_patterns(self):
        return self.__private_Suences_patterns()

#--------------:
print(SPR([3, 1, -1, -2]).public_Suences_patterns() == False)
print(SPR([-3, 3, 1]).public_Suences_patterns() == False)
print(SPR([1, 1, 1]).public_Suences_patterns() == True)
