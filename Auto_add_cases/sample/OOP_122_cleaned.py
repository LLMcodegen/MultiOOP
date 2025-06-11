
class RNE:
    def __init__(self, n):
        self.n = n
    def __private_remaining_numbers(self, arr):
        while len(arr) > 1:
            arr = arr[1::2]
            if len(arr) > 1:
                arr = arr[::-1][1::2][::-1]
        return arr[0]
    def public_remaining_numbers(self):
        arr = list(range(1, self.n + 1))
        return self.__private_remaining_numbers(arr)

#--------------:
print(RNE(6).public_remaining_numbers() == 4)
print(RNE(7).public_remaining_numbers() == 4)
print(RNE(8).public_remaining_numbers() == 6)
