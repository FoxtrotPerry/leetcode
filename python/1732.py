# O(n)


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        elevation = 0
        max_elevation = 0
        for change in gain:
            elevation += change
            max_elevation = max(max_elevation, elevation)
        return max_elevation
