
class NDG:
    def __init__(self, digits):
        self.digits = digits
class SN_NDG(NDG):
    def __init__(self, digits, n):
        super().__init__(digits)
        self.n = n
    def Non_decreasing(self):
        digit_ints = [int(d) for d in self.digits]
        n_str = str(self.n)
        n_len = len(n_str)
        def count_numbers_with_length(length):
            if length == 0:
                return 1
            return len(self.digits) ** length
        count = sum(count_numbers_with_length(length) for length in range(1, n_len))
        def count_valid_numbers(index, prefix):
            if index == n_len:
                return 1
            count = 0
            for d in digit_ints:
                if d < int(n_str[index]):
                    count += len(self.digits) ** (n_len - index - 1)
                elif d == int(n_str[index]):
                    count += count_valid_numbers(index + 1, prefix + str(d))
            return count
        count += count_valid_numbers(0, "")  
        return count

#--------------:
print(SN_NDG(['1', '2', '3'], 400).Non_decreasing() == 39)
print(SN_NDG(['1', '2', '3'], 500).Non_decreasing() == 39)
print(SN_NDG(['1', '2', '3'], 600).Non_decreasing() == 39)
