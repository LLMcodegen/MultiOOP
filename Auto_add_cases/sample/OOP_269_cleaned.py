
class MPT:
    def __init__(self, difficulty):
        self.difficulty = difficulty
class SN_MPT(MPT):
    def __init__(self, difficulty, profit, worker):
        super().__init__(difficulty)
        self.profit = profit
        self.worker = worker
    def Maximum_profit(self):
        jobs = sorted(zip(self.difficulty, self.profit))
        self.worker.sort()
        max_profit = 0
        i = 0
        current_max_profit = 0
        for ability in self.worker:
            while i < len(jobs) and jobs[i][0] <= ability:
                current_max_profit = max(current_max_profit, jobs[i][1])
                i += 1
            max_profit += current_max_profit
        return max_profit

#--------------:
print(SN_MPT([1, 2, 3], [10, 20, 30], [2, 3, 1]).Maximum_profit() == 60)
print(SN_MPT([1, 2, 3], [10, 20, 30], [3, 1, 2]).Maximum_profit() == 60)
print(SN_MPT([1, 2, 3], [10, 20, 30], [3, 2, 1]).Maximum_profit() == 60)
