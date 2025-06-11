class FMIS:
    def find_matching_items(self, haystack, needle):
        if not needle:
            return 0
        if len(needle) > len(haystack):
            return -1
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1
#--------------:
print(FMIS().find_matching_items("deep learning", "deep") == 0)
print(FMIS().find_matching_items("data analysis", "analysis") == 5)
print(FMIS().find_matching_items("python programming", "python") == 0)
