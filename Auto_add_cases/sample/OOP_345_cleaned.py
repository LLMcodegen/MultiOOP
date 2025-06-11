
class NIG:
    def __init__(self, n):
        self.n = n
class SN_NIG(NIG):
    def __init__(self, n, k):
        super().__init__(n)
        self.k = k
    def nonnegative_integer(self):
        if self.n == 1:
            return [i for i in range(10)]
        results = []
        queue = [i for i in range(1, 10)]
        for _ in range(self.n - 1):
            next_queue = []
            for num in queue:
                last_digit = num % 10
                next_digits = set()
                if last_digit + self.k <= 9:
                    next_digits.add(last_digit + self.k)
                if last_digit - self.k >= 0:
                    next_digits.add(last_digit - self.k)
                for next_digit in next_digits:
                    new_num = num * 10 + next_digit
                    next_queue.append(new_num)
            queue = next_queue
        return sorted(queue)

#--------------:
print(SN_NIG(3, 3).nonnegative_integer() == [141, 147, 252, 258, 303, 363, 369, 414, 474, 525, 585, 630, 636, 696, 741, 747, 852, 858, 963, 969])
print(SN_NIG(4, 1).nonnegative_integer() == [1010, 1012, 1210, 1212, 1232, 1234, 2101, 2121, 2123, 2321, 2323, 2343, 2345, 3210, 3212, 3232, 3234, 3432, 3434, 3454, 3456, 4321, 4323, 4343, 4345, 4543, 4545, 4565, 4567, 5432, 5434, 5454, 5456, 5654, 5656, 5676, 5678, 6543, 6545, 6565, 6567, 6765, 6767, 6787, 6789, 7654, 7656, 7676, 7678, 7876, 7878, 7898, 8765, 8767, 8787, 8789, 8987, 8989, 9876, 9878, 9898])
print(SN_NIG(4, 2).nonnegative_integer() == [1313, 1353, 1357, 2020, 2024, 2420, 2424, 2464, 2468, 3131, 3135, 3531, 3535, 3575, 3579, 4202, 4242, 4246, 4642, 4646, 4686, 5313, 5353, 5357, 5753, 5757, 5797, 6420, 6424, 6464, 6468, 6864, 6868, 7531, 7535, 7575, 7579, 7975, 7979, 8642, 8646, 8686, 9753, 9757, 9797])
