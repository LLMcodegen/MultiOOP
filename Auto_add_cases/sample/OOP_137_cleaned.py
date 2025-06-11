
class LSR:
    def __init__(self, s, k):
        self.s = s
        self.k = k
    def __private_Longest_substring(self):
        max_len = 0
        count = {}
        left = 0
        for right in range(len(self.s)):
            count[self.s[right]] = count.get(self.s[right], 0) + 1
            if (right - left + 1) - max(count.values()) > self.k:
                count[self.s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len
    def public_Longest_substring(self):
        return self.__private_Longest_substring()

#--------------:
print(LSR("AAAAA", 2).public_Longest_substring() == 5)
print(LSR("AABAC", 2).public_Longest_substring() == 5)
print(LSR("AABBCC", 1).public_Longest_substring() == 3)
