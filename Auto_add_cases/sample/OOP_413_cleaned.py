
class DSN:
    def __init__(self, text):
        self.text = text
class SN_DSN(DSN):
    def __init__(self, text):
        super().__init__(text)
    def Duplicate_string(self):
        from collections import Counter
        text = self.text
        n = len(text)
        max_len = 0
        count = Counter(text)
        blocks = []
        i = 0
        while i < n:
            ch = text[i]
            j = i
            while j < n and text[j] == ch:
                j += 1
            blocks.append((ch, i, j - i))
            max_len = max(max_len, j - i)
            i = j
        for i in range(len(blocks)):
            ch, start, length = blocks[i]
            total_ch = count[ch]
            if total_ch > length:
                max_len = max(max_len, length + 1)
            if i + 2 < len(blocks) and blocks[i + 2][0] == ch and blocks[i + 1][2] == 1:
                merged_length = blocks[i][2] + blocks[i + 2][2]
                if total_ch > merged_length:
                    merged_length += 1
                max_len = max(max_len, merged_length)
        return max_len

#--------------:
print(SN_DSN("aabbaa").Duplicate_string() == 3)
print(SN_DSN("aabbcc").Duplicate_string() == 2)
print(SN_DSN("aabbccdd").Duplicate_string() == 2)
