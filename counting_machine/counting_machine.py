class CountingMachine:
    def __init__(self, count=0):
        self.count = count

    def inc(self):
        self.count += 1

    def dec(self):
        self.count -= 1
