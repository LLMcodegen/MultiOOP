
class CDC:
    def __init__(self, s):
        self.s = s
class SN_CDC(CDC):
    def __init__(self, s, c):
        super().__init__(s)
        self.c = c
    def Character_distance(self):
        s = self.s
        c = self.c
        n = len(s)
        answer = [float('inf')] * n
        prev_position = -float('inf')
        for i in range(n):
            if s[i] == c:
                prev_position = i
            answer[i] = i - prev_position
        prev_position = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev_position = i
            answer[i] = min(answer[i], prev_position - i)
        return answer

#--------------:
print(SN_CDC("abcde", "e").Character_distance() == [4, 3, 2, 1, 0])
print(SN_CDC("abcde", "a").Character_distance() == [0, 1, 2, 3, 4])
print(SN_CDC("a", "a").Character_distance() == [0])
