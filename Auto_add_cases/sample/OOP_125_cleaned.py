
class LST:
    def __init__(self, s, k):
        self.s = s
        self.k = k
    def __private_Longest_substring(self):
        def longest_substring_helper(s, k):
            if len(s) < k:
                return 0
            char_count = {}
            for char in s:
                char_count[char] = char_count.get(char, 0) + 1
            for char, count in char_count.items():
                if count < k:
                    return max(longest_substring_helper(sub_s, k) for sub_s in s.split(char))
            return len(s)
        return longest_substring_helper(self.s, self.k)

    def public_Longest_substring(self):
        return self.__private_Longest_substring()

#--------------:
print(LST("aaabbbccc", 3).public_Longest_substring() == 9)
print(LST("aabbcc", 7).public_Longest_substring() == 0)
print(LST("abcde", 1).public_Longest_substring() == 5)
