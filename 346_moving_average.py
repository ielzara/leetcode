from typing import List


class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.stream = []
        self.sum = 0

    def next(self, val: int) -> float:
        self.stream.append(val)
        self.sum += val
        if len(self.stream) > self.size:
            self.sum -= self.stream.pop(0)
        return self.sum / len(self.stream)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
