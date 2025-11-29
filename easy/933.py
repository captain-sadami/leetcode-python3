from collections import deque

class RecentCounter:

    def __init__(self):
        self.counter = deque()

    def ping(self, t: int) -> int:
        while self.counter and t - self.counter[0] > 3000:
            self.counter.popleft()
        self.counter.append(t)
        return len(self.counter)
