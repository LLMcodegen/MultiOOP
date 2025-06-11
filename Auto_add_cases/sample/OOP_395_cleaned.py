
class SSU:
    def __init__(self, s: str):
        self.s = s
class SN_SSU(SSU):
    def smallest_subsequence(self) -> str:
        last_occurrence = {char: idx for idx, char in enumerate(self.s)}
        stack = []
        seen = set()
        for idx, char in enumerate(self.s):
            if char not in seen:
                while stack and stack[-1] > char and idx < last_occurrence[stack[-1]]:
                    seen.remove(stack.pop())
                stack.append(char)
                seen.add(char)
        return ''.join(stack)

#--------------:
print(SN_SSU("leetcode").smallest_subsequence() == "letcod")
print(SN_SSU("cdbca").smallest_subsequence() == "cdba")
print(SN_SSU("zxzytyz").smallest_subsequence() == "xtyz")
