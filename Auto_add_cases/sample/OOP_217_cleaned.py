
from collections import Counter
from functools import lru_cache

class SW:
    def __init__(self, stickers, target):
        self.stickers = stickers
        self.target = target
    def _private_Sticker_Words(self):
        sticker_counters = [Counter(sticker) for sticker in self.stickers]
        @lru_cache(None)
        def dp(target):
            if not target:
                return 0
            target_counter = Counter(target)
            res = float('inf')
            for sticker_counter in sticker_counters:
                if target[0] in sticker_counter:
                    remaining_target = target_counter - sticker_counter
                    remaining_target_str = ''.join(sorted(remaining_target.elements()))
                    res = min(res, 1 + dp(remaining_target_str))
            return res
        result = dp(self.target)
        return result if result != float('inf') else -1
    def public_Sticker_Words(self):
        return self._private_Sticker_Words()

#--------------:
print(SW(["a", "b"], "aabb").public_Sticker_Words() == 4)
print(SW(["a", "b"], "ab").public_Sticker_Words() == 2)
print(SW(["a", "b"], "abc").public_Sticker_Words() == -1)
