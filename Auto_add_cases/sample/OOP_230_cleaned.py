
class LS:
    def __init__(self, head, k):
        self.head = head
        self.k = k
    def __private_List_separation(self):
        length = len(self.head)
        part_size = length // self.k
        larger_parts = length % self.k
        parts = []
        start = 0
        for i in range(self.k):
            size = part_size + (1 if i < larger_parts else 0)
            if size > 0:
                parts.append(self.head[start:start + size])
            else:
                parts.append([])
            start += size
        return parts
    def public_List_separation(self):
        return self.__private_List_separation()

#--------------:
print(LS([1, 2, 3, 4, 5, 6, 7, 8], 3).public_List_separation() == [[1, 2, 3], [4, 5, 6], [7, 8]])
print(LS([1, 2, 3, 4, 5, 6, 7, 8, 9], 3).public_List_separation() == [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(LS([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4).public_List_separation() == [[1, 2, 3], [4, 5, 6], [7, 8], [9, 10]])
