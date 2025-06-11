class DSBCD:
    def distribute_candie(self, ratings):
        n = len(ratings)
        if n == 0:
            return 0
        candies = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        return sum(candies)
#--------------:
print(DSBCD().distribute_candie([5, 4, 3, 2, 1]) == 15)
print(DSBCD().distribute_candie([1, 2, 3, 4, 4, 3, 2, 1]) == 20)
print(DSBCD().distribute_candie([1]) == 1)