
class IIFI:
    def __init__(self, s1, n1, s2, n2):
        self.s1 = s1
        self.n1 = n1
        self.s2 = s2
        self.n2 = n2
    def __private_Italic_tion(self):
        def can_obtain(s1, s2):
            i, j = 0, 0
            while i < len(s1) and j < len(s2):
                if s1[i] == s2[j]:
                    i += 1
                j += 1
            return i == len(s1)
        str1 = self.s1 * self.n1
        str2 = self.s2 * self.n2
        if not can_obtain(str2, str1):
            return 0
        left, right = 0, len(str1) // len(str2)
        while left <= right:
            mid = (left + right) // 2
            if can_obtain(str2 * mid, str1):
                left = mid + 1
            else:
                right = mid - 1
        return right
    def public_Italic_tion(self):
        return self.__private_Italic_tion()

#--------------:
print(IIFI("aaa", 5, "a", 3).public_Italic_tion() == 5)
print(IIFI("abc", 3, "abc", 1).public_Italic_tion() == 3)
print(IIFI("ab", 2, "a", 5).public_Italic_tion() == 0)
