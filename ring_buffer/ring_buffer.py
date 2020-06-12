class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []
        self.oldest = 0

    def append(self, item):
        if len(self.buffer) == self.capacity:
            self.buffer[self.oldest] = item

            if self.oldest == self.capacity - 1:
                self.oldest = 0
            else:
                self.oldest+=1
        else:
            self.buffer.append(item)

    def get(self):
        new_list = []
        for item in self.buffer:
            if item is not None:
                new_list.append(item)
        return new_list