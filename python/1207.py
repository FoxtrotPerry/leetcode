from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for num in arr:
            if d.get(num) is not None:
                d[num] += 1
            else:
                d[num] = 1
        return len(set(d.values())) == len(d.values())


print(Solution.uniqueOccurrences(None, [1, 2, 2, 1, 1, 3]))
