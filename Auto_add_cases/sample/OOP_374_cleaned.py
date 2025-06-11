
class BAY:
    def __init__(self, queries):
        self.queries = queries
class SN_BAY(BAY):
    def __init__(self, queries, pattern):
        super().__init__(queries)
        self.pattern = pattern
    def boolean_array(self):
        result = []
        for query in self.queries:
            result.append(self.matches(query, self.pattern))
        return result
    def matches(self, query, pattern):
        i, j = 0, 0
        while i < len(query):
            if j < len(pattern) and query[i] == pattern[j]:
                i += 1
                j += 1
            elif query[i].islower():
                i += 1
            else:
                return False
        return j == len(pattern)

#--------------:
print(SN_BAY(["Python", "Java", "JavaScript", "Ruby", "Swift"], "Py").boolean_array() == [True, False, False, False, False])
print(SN_BAY(["Python", "Java", "JavaScript", "Ruby", "Swift"], "Ja").boolean_array() == [False, True, False, False, False])
print(SN_BAY(["Python", "Java", "JavaScript", "Ruby", "Swift"], "Ru").boolean_array() == [False, False, False, True, False])
