
class PPM:
    def __init__(self, N):
        self.N = N
class SN_PPM(PPM):
    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    def is_palindrome(self, num):
        return str(num) == str(num)[::-1]
    def prime_palindromes(self):
        num = self.N
        while True:
            if self.is_palindrome(num) and self.is_prime(num):
                return num
            num += 1

#--------------:
print(SN_PPM(3).prime_palindromes() == 3)
print(SN_PPM(4).prime_palindromes() == 5)
print(SN_PPM(5).prime_palindromes() == 5)
