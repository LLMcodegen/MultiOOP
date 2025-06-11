
class ESI:
    def __init__(self, text: str):
        self.text = text
class SN_ESI(ESI):
    def empty_string(self) -> int:
        text = self.text
        n = len(text)
        left = 0
        right = n
        k = 0
        while left < right:
            found = False
            for length in range(1, (right - left) // 2 + 1):
                prefix = text[left:left+length]
                suffix = text[right-length:right]
                if prefix == suffix:
                    k += 2
                    left += length
                    right -= length
                    found = True
                    break
            if not found:
                k += 1
                break
        return k

#--------------:
print(SN_ESI("aa").empty_string() == 2)
print(SN_ESI("aaa").empty_string() == 3)
print(SN_ESI("abba").empty_string() == 4)
