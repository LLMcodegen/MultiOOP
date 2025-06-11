from typing import List
class UQPTT:
    def unique_permutations(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path, choices):
            if not choices:
                result.append(path)
                return
            seen = set()
            for i in range(len(choices)):
                if choices[i] in seen:
                    continue
                seen.add(choices[i])
                backtrack(path + [choices[i]], choices[:i] + choices[i+1:])
        result = []
        backtrack([], sorted(nums))
        return result
#--------------:
#--------------:
print(UQPTT().unique_permutations([1, 2, 2, 3]) == [[1, 2, 2, 3], [1, 2, 3, 2], [1, 3, 2, 2], [2, 1, 2, 3], [2, 1, 3, 2], [2, 2, 1, 3], [2, 2, 3, 1], [2, 3, 1, 2], [2, 3, 2, 1], [3, 1, 2, 2], [3, 2, 1, 2], [3, 2, 2, 1]])
print(UQPTT().unique_permutations([7, 8]) == [[7, 8], [8, 7]])
print(UQPTT().unique_permutations([5, 5, 5]) == [[5, 5, 5]])
