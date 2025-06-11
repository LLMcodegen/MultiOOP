class STPD:
    def __init__(self):
        pass
    def Shortest_Palindrome(self, s: str) -> str:
        if not s:
            return s
        def is_palindrome(sub):
            return sub == sub[::-1]
        longest_prefix_palindrome = ""
        for i in range(len(s)):
            if is_palindrome(s[:i + 1]):
                longest_prefix_palindrome = s[:i + 1]
        if longest_prefix_palindrome == s:
            return s
        prepend = s[len(longest_prefix_palindrome):][::-1]
        return prepend + s
#--------------:
print(STPD().Shortest_Palindrome("xyz") == "zyxyz")
print(STPD().Shortest_Palindrome("palindrome") == "emordnilapalindrome")
print(STPD().Shortest_Palindrome("a") == "a")
