class PDSB:
    def __init__(self):
        pass
    def pa_substring(self, s: str) -> str:
        if not s:
            return ""
        def expand_around_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        longest_palindrome = ""
        for i in range(len(s)):
            palindrome1 = expand_around_center(i, i)
            palindrome2 = expand_around_center(i, i + 1)
            if len(palindrome1) > len(longest_palindrome):
                longest_palindrome = palindrome1
            if len(palindrome2) > len(longest_palindrome):
                longest_palindrome = palindrome2
        return longest_palindrome
#--------------:
print(PDSB().pa_substring("noon") == "noon")
print(PDSB().pa_substring("forgeeksskeegfor") == "geeksskeeg")