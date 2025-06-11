class JTA:
    def judging_the_array(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
#--------------:
#--------------:
print(JTA().judging_the_array([14, 15, 16, 17]) == False)
print(JTA().judging_the_array([1, 2, 2, 2]) == True)
print(JTA().judging_the_array([100, 200, 300, 400, 500]) == False)
