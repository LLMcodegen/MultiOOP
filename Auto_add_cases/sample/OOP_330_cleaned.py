
class ESU:
    def __init__(self, s: str):
        self.s = s
class SN_ESU(ESU):
    def empty_subsequence(self):
        subsequences = set()
        def generate_subsequences(index, current_subsequence):
            if index == len(self.s):
                if current_subsequence:
                    subsequences.add(current_subsequence)
                return
            generate_subsequences(index + 1, current_subsequence + self.s[index])
            generate_subsequences(index + 1, current_subsequence)
        generate_subsequences(0, "")
        return len(subsequences)

#--------------:
print(SN_ESU("aabb").empty_subsequence() == 8)
print(SN_ESU("abac").empty_subsequence() == 13)
print(SN_ESU("abca").empty_subsequence() == 14)
