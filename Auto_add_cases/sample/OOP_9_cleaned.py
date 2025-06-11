class LCMP:
    def longest_common_prefix(self, strs):
        if not strs:
            return ""
        prefix = strs[0]
        for string in strs[1:]:
            while not string.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
#--------------:
print(LCMP().longest_common_prefix(["single"]) == "single")
print(LCMP().longest_common_prefix(["prefix", "prefixation", "prefab"]) == "pref")
print(LCMP().longest_common_prefix(["unity", "universe", "uniform"]) == "uni")
