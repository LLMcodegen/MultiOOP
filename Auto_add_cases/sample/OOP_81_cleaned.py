
class PCT:
    def __init__(self, citations):
        self.citations = citations
    def __private_Paper_cited(self):
        sorted_citations = sorted(self.citations, reverse=True)
        h_index = 0
        for i, citation_count in enumerate(sorted_citations):
            if citation_count >= i + 1:
                h_index = i + 1
            else:
                break
        return h_index
    def public_Paper_cited(self):
        return self.__private_Paper_cited()

#--------------:
print(PCT([6, 6, 6, 6, 6, 6]).public_Paper_cited() == 6)
print(PCT([0, 1, 2, 3, 4]).public_Paper_cited() == 2)
print(PCT([4, 4, 4, 4, 4]).public_Paper_cited() == 4)
