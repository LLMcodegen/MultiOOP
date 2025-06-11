
class MCT:
    def __init__(self, costs):
        self.costs = costs
class SN_MCT(MCT):
    def Minimum_cost(self):
        n = len(self.costs) // 2
        diffs = [(cost[0] - cost[1], cost) for cost in self.costs]
        diffs.sort()
        total_cost = 0
        for i in range(n):
            total_cost += diffs[i][1][0]
        for i in range(n, 2 * n):
            total_cost += diffs[i][1][1]
        return total_cost

#--------------:
print(SN_MCT([[1, 100], [2, 200], [3, 300], [4, 400]]).Minimum_cost() == 307)
print(SN_MCT([[10, 10], [20, 20], [30, 30], [40, 40]]).Minimum_cost() == 100)
print(SN_MCT([[100, 10], [200, 20], [300, 30], [400, 40]]).Minimum_cost() == 370)
