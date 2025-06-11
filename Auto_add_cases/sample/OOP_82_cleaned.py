
class AOD:
    def __init__(self, citations):
        self.citations = citations
    def __private_Paper_cited(self):
        n = len(self.citations)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if self.citations[mid] >= n - mid:
                right = mid - 1
            else:
                left = mid + 1
        return n - left
    def public_ascend_order(self):
        return self.__private_Paper_cited()

#--------------:
print(AOD([0, 2, 3, 4, 5]).public_ascend_order() == 3)
print(AOD([1, 4, 6, 7]).public_ascend_order() == 3)
print(AOD([0, 1, 2, 4, 6]).public_ascend_order() == 2)
