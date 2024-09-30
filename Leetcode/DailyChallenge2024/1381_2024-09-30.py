class CustomStack:
    def __init__(self, maxSize: int):
        self.stack = []
        self.incre = []
        self.curr_size = 0
        self.max_size = maxSize

    def push(self, x: int) -> None:
        if self.curr_size < self.max_size:
            self.stack.append(x)
            self.incre.append(0)
            self.curr_size += 1

    def pop(self) -> int:
        if self.curr_size:
            self.curr_size -= 1
            if len(self.incre) > 1:
                self.incre[-2] += self.incre[-1]
            return self.stack.pop() + self.incre.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        curr_incre = min(self.curr_size, k)
        if curr_incre > 0:
            self.incre[curr_incre - 1] += val
