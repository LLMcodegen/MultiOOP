class GTAC:
    def additive_combination(self, k, n):
        result = []
        def backtrack(start, path, remaining_sum):
            if len(path) == k:
                if remaining_sum == 0:
                    result.append(path[:])
                return
            for i in range(start, 10):
                if i > remaining_sum:
                    break
                path.append(i)
                backtrack(i + 1, path, remaining_sum - i)
                path.pop()
        backtrack(1, [], n)
        return result
#--------------:
print(GTAC().additive_combination(3, 10) == [[1, 2, 7], [1, 3, 6], [1, 4, 5], [2, 3, 5]])
print(GTAC().additive_combination(3, 15) == [[1, 5, 9], [1, 6, 8], [2, 4, 9], [2, 5, 8], [2, 6, 7], [3, 4, 8], [3, 5, 7], [4, 5, 6]])
print(GTAC().additive_combination(4, 10) == [[1, 2, 3, 4]])
