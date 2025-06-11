class JS:
    def Judgment_Splicing(self, s: str, wordDict: list) -> bool:
        wordSet = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break
        return dp[len(s)]
#--------------:
print(JS().Judgment_Splicing("catsanddogs", ["cats", "dogs", "and", "sand"]) == True)
print(JS().Judgment_Splicing("helloworld", ["hello", "world"]) == True)
print(JS().Judgment_Splicing("applepie", ["apple", "pie"]) == True)
