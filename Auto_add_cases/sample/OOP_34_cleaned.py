class NNTI:
    def __init__(self):
        pass
    @staticmethod
    def non_negative_integer(arr):
        carry = 1
        for i in range(len(arr) - 1, -1, -1):
            new_digit = arr[i] + carry
            if new_digit == 10:
                arr[i] = 0
                carry = 1
            else:
                arr[i] = new_digit
                carry = 0
                break
        if carry == 1:
            arr.insert(0, 1)
        return arr
#--------------:
#--------------:
print(NNTI().non_negative_integer([0, 0, 1]) == [0, 0, 2])
print(NNTI().non_negative_integer([5]) == [6])
print(NNTI().non_negative_integer([1, 0, 0, 9]) == [1, 0, 1, 0])
