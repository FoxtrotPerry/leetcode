from collections import deque
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        d = deque()
        d.append(asteroids[0])
        i = 1
        while i < len(asteroids):
            if len(d) > 0:
                last_direction = "left" if d[-1] < 0 else "right"
                curr_direction = "left" if asteroids[i] < 0 else "right"
                # detect collision and do something about it
                if last_direction == "right" and curr_direction == "left":
                    if abs(d[-1]) < abs(asteroids[i]):
                        d.pop()
                        # d.append(asteroids[i])
                        # i += 1
                    elif abs(d[-1]) == abs(asteroids[i]):
                        d.pop()
                        i += 1
                    else:
                        i += 1
                else:
                    d.append(asteroids[i])
                    i += 1
            else:
                d.append(asteroids[i])
                i += 1
        return list(d)


# print(Solution.asteroidCollision(None, [5, 10, -5]))
# print(Solution.asteroidCollision(None, [8, -8]))
# print(Solution.asteroidCollision(None, [10, 2, -5]))
print(Solution.asteroidCollision(None, [1, -2, -2, -2]))
