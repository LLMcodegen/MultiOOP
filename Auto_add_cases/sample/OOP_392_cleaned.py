
class ANS:
    def __init__(self, arr1):
        self.arr1 = arr1
class SN_ANS(ANS):
    def __init__(self, arr1, arr2):
        super().__init__(arr1)
        self.arr2 = arr2
    def Adding_Numbers(self):
        def negabinary_to_decimal(arr):
            decimal = 0
            for i, digit in enumerate(reversed(arr)):
                decimal += digit * (-2) ** i
            return decimal
        def decimal_to_negabinary(decimal):
            if decimal == 0:
                return [0]
            negabinary = []
            while decimal != 0:
                remainder = decimal % -2
                decimal = decimal // -2
                if remainder < 0:
                    remainder += 2
                    decimal += 1
                negabinary.insert(0, remainder)
            return negabinary
        decimal_arr1 = negabinary_to_decimal(self.arr1)
        decimal_arr2 = negabinary_to_decimal(self.arr2)
        result_decimal = decimal_arr1 + decimal_arr2
        result_negabinary = decimal_to_negabinary(result_decimal)
        return result_negabinary

#--------------:
print(SN_ANS([1, 1], [1, 1]).Adding_Numbers() == [1, 0])
print(SN_ANS([1, 0], [1, 0]).Adding_Numbers() == [1, 1, 0, 0])
print(SN_ANS([1], [1]).Adding_Numbers() == [1, 1, 0])
