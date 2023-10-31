from collections import deque


class RecentCounter:
    def __init__(self):
        # init a deque
        # https://docs.python.org/3/library/collections.html#collections.deque
        self.q = deque()

    def ping(self, t: int) -> int:
        # append the time (t) to the deque
        self.q.append(t)

        # while there are still items in the deque that are older than
        # t - 3000ms, pop the oldest items in the deque
        while t - self.q[0] > 3000:
            self.q.popleft()

        # return the lenth of the queue after getting rid of the stale entries
        return len(self.q)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
