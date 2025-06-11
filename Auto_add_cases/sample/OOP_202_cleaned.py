
class PS:
    def __init__(self, s):
        self.s = s
    def __private_Palindrome_substring(self):
        def is_palindrome(sub):
            return sub == sub[::-1]
        count = 0
        length = len(self.s)
        for i in range(length):
            for j in range(i + 1, length + 1):
                if is_palindrome(self.s[i:j]):
                    count += 1
        return count
    def public_Palindrome_substring(self):
        return self.__private_Palindrome_substring()

#--------------:
print(PS("abcd").public_Palindrome_substring() == 4)
print(PS("a").public_Palindrome_substring() == 1)
print(PS("abba").public_Palindrome_substring() == 6)
