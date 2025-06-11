class CS:
    def Constructing_Sentences(self, s, wordDict):
        def backtrack(start):
            if start == len(s):
                return [[]]
            if start in memo:
                return memo[start]
            sentences = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordDict:
                    for subsentence in backtrack(end):
                        sentences.append([word] + subsentence)
            memo[start] = sentences
            return sentences
        memo = {}
        wordDict = set(wordDict)
        result = backtrack(0)
        return [' '.join(words) for words in result]
#--------------:
print(CS().Constructing_Sentences("workfromhome", ["work", "from", "home"]) == ["work from home"])
print(CS().Constructing_Sentences("iloveicecream", ["i", "love", "ice", "cream", "icecream"]) == ["i love ice cream", "i love icecream"])
print(CS().Constructing_Sentences("themanran", ["the", "man", "ran"]) == ["the man ran"])
