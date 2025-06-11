
class MPRD:
    def __init__(self, n):
        self.n = n
    def __private_Maximum_palindrome(self):
        max_num = 10**self.n - 1
        min_num = 10**(self.n - 1)
        max_palindrome = 0
        for i in range(max_num, min_num - 1, -1):
            for j in range(i, min_num - 1, -1):
                product = i * j
                if str(product) == str(product)[::-1]:  # Check if product is a palindrome
                    max_palindrome = max(max_palindrome, product)
        return max_palindrome
    def public_Maximum_palindrome(self):
        return self.__private_Maximum_palindrome()

#--------------:
print(MPRD(1).public_Maximum_palindrome() == 9)
print(MPRD(2).public_Maximum_palindrome() == 9009)
print(MPRD(3).public_Maximum_palindrome() == 906609)
