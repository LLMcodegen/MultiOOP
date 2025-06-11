import re
class RLMH:
    def rule_matching(self, s: str, p: str) -> bool:
        return re.fullmatch(p, s) is not None
#--------------:
print(RLMH().rule_matching("ab", ".*c") == False)
print(RLMH().rule_matching("ab", "a*b*") == True)
print(RLMH().rule_matching("aaa", "a*a") == True)
