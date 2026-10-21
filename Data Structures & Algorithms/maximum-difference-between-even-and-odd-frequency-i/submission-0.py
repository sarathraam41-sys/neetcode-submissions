from collections import Counter
import math
class Solution:
    def maxDifference(self, s: str) -> int:
        counts = Counter(s)  
        max_odd = 0
        min_even = math.inf
        for freq in counts.values():
            if freq % 2 == 1:
                max_odd = max(max_odd, freq)
            else:
                min_even = min(min_even, freq)
        return max_odd - min_even
