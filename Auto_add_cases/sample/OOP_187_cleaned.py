
class PI:
    def __init__(self, n):
        self.n = n
    def __private_Palindrome_integer(self):

        n = self.n
        length = len(n)
        number = int(n)
        if length == 1:
            return str(number - 1) if number > 0 else str(number + 1)
        def get_palindromes():
            prefix = n[:(length + 1) // 2]
            prefix_num = int(prefix)
            candidate1 = str(prefix_num) + str(prefix_num)[:length // 2][::-1]
            candidate2 = str(prefix_num + 1) + str(prefix_num + 1)[:length // 2][::-1]
            candidate3 = str(prefix_num - 1) + str(prefix_num - 1)[:length // 2][::-1]
            candidate4 = '9' * (length - 1)
            candidate5 = '1' + '0' * (length - 1) + '1'
            return [candidate1, candidate2, candidate3, candidate4, candidate5]
        candidates = get_palindromes()
        candidates = [int(c) for c in candidates if c != n]
        closest_palindrome = min(candidates, key=lambda x: (abs(x - number), x))
        return str(closest_palindrome)
    def public_Palindrome_integer(self):
        return self.__private_Palindrome_integer()

#--------------:
print(PI("45654").public_Palindrome_integer() == "45554")
print(PI("10").public_Palindrome_integer() == "9")
print(PI("11").public_Palindrome_integer() == "9")