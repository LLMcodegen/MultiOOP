
class MTL:
    def __init__(self, arr):
        self.arr = arr
class SN_MTL(MTL):
    def Maximum_turbulence(self):
        n = len(self.arr)
        if n < 2:
            return n
        max_length = 1
        current_length = 1
        for i in range(1, n):
            if (self.arr[i] > self.arr[i - 1] and (i == 1 or self.arr[i - 1] <= self.arr[i - 2])) or \
               (self.arr[i] < self.arr[i - 1] and (i == 1 or self.arr[i - 1] >= self.arr[i - 2])):
                current_length += 1
            else:
                current_length = 2 if self.arr[i] != self.arr[i - 1] else 1
            max_length = max(max_length, current_length)
        return max_length

#--------------:
print(SN_MTL([1, 2, 1, 2, 1]).Maximum_turbulence() == 5)
print(SN_MTL([1, 1, 1, 1, 1]).Maximum_turbulence() == 1)
print(SN_MTL([1, 3, 2, 4, 5]).Maximum_turbulence() == 4)
