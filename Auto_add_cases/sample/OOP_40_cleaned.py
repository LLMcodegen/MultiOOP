class FTMPA:
    def Minimum_Path(self, triangle):
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]
#--------------:
print(FTMPA().Minimum_Path([[1], [2, 2], [1, 1, 1], [0, 0, 0, 0]]) == 4)
print(FTMPA().Minimum_Path([[10], [15, 25], [30, 35, 40], [45, 50, 55, 60]]) == 100)
print(FTMPA().Minimum_Path([[1], [5, 1], [2, 1, 4], [1, 2, 1, 5]]) == 4)
