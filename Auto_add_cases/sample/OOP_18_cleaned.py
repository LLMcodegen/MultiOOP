class NCBT:
    def numeric_combination(self, candidates, target):
        def backtrack(start, target, path):
            if target == 0:
                result.append(path.copy())
                return
            if target < 0:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                backtrack(i + 1, target - candidates[i], path)
                path.pop()
        candidates.sort()
        result = []
        backtrack(0, target, [])
        return result
#--------------:
print(NCBT().numeric_combination([2, 2, 2, 2, 5], 7) == [[2, 5]])
print(NCBT().numeric_combination([1, 3, 3, 3, 5], 6) == [[1, 5], [3, 3]])  # [[1, 5], [3, 3]]
print(NCBT().numeric_combination([1, 1, 1, 2, 5], 6) == [[1, 5]])  # [[1, 5]]