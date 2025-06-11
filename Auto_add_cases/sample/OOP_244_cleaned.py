
class SS:
    def __init__(self, arr):
        self.arr = arr
    def __private_Sort_separately(self) -> int:
        max_so_far = 0
        blocks = 0
        for i in range(len(self.arr)):
            max_so_far = max(max_so_far, self.arr[i])
            if max_so_far == i:
                blocks += 1
        return blocks
    def public_Sort_separately(self) -> int:
        return self.__private_Sort_separately()

#--------------:
print(SS([3, 2, 1, 0, 4]).public_Sort_separately() == 2)
print(SS([0, 2, 1, 4, 3]).public_Sort_separately() == 3)
print(SS([1, 0, 3, 2, 4]).public_Sort_separately() == 3)
