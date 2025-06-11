
class DOD:
    def __init__(self, n):
        self.n = n
    def __private_Dictionary_order(self):
        def generate_numbers(n):
            if n < 10:
                return list(range(1, n + 1))
            else:
                result = []
                for i in range(1, 10):
                    result.append(i)
                    result.extend(generate_numbers_starting_with(i, n))
                return result
        def generate_numbers_starting_with(prefix, max_value):
            result = []
            prefix *= 10
            for i in range(10):
                if prefix + i <= max_value:
                    result.append(prefix + i)
                    result.extend(generate_numbers_starting_with(prefix + i, max_value))
            return result
        return generate_numbers(self.n)
    def public_Dictionary_order(self):
        return self.__private_Dictionary_order()

#--------------:
print(DOD(3).public_Dictionary_order() == [1, 2, 3])
print(DOD(15).public_Dictionary_order() == [1, 10, 11, 12, 13, 14, 15, 2, 3, 4, 5, 6, 7, 8, 9])
print(DOD(9).public_Dictionary_order() == [1, 2, 3, 4, 5, 6, 7, 8, 9])
