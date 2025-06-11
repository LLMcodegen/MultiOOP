
class AL:
    def __init__(self, n, k):
        self.n = n
        self.k = k
    def _private_Answer_List(self):
        answer = []
        if self.k == 1:
            return list(range(1, self.n + 1))
        for i in range(self.k + 1):
            if i % 2 == 0:
                answer.append(i // 2 + 1)
            else:
                answer.append(self.k + 1 - (i // 2))
        remaining = list(range(self.k + 2, self.n + 1))
        if self.k % 2 == 0:
            answer.extend(remaining)
        else:
            answer.extend(reversed(remaining))
        return answer
    def public_Answer_List(self):
        return self._private_Answer_List()

#--------------:
print(AL(5, 3).public_Answer_List() == [1, 4, 2, 3, 5])
print(AL(4, 2).public_Answer_List() == [1, 3, 2, 4])
print(AL(9, 6).public_Answer_List() == [1, 7, 2, 6, 3, 5, 4, 8, 9])
