
class JM:
    def __init__(self, matrix):
        self.matrix = matrix
    def __private_judgment_matrix(self):
        m = len(self.matrix)
        n = len(self.matrix[0])
        for i in range(m - 1):
            for j in range(n - 1):
                if self.matrix[i][j] != self.matrix[i + 1][j + 1]:
                    return False
        return True
    def public_judgment_matrix(self):
        return self.__private_judgment_matrix()

#--------------:
print(JM([[1, 2], [3, 1], [4, 2]]).public_judgment_matrix() == False)
print(JM([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2], [8, 9, 5, 1]]).public_judgment_matrix() == True)
print(JM([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2], [8, 9, 5, 2]]).public_judgment_matrix() == False)
