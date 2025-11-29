class RecentCounter:

    def __init__(self):
        self.counter = []

    def ping(self, t: int) -> int:
        self.counter = [c for c in self.counter if t - c <= 3000]
        
        self.counter.append(t)
        return len(self.counter)
