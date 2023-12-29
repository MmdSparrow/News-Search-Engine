class PriorityQueueWithFixedLength:
    LENGTH = 50

    def __init__(self, capacity: int = LENGTH):
        self.capacity = capacity
        # (word, frequency)
        self.queue = []

    def push(self, key, value):
        # if word was in queue update it's frequency
        index_temp = self.__contain(key)
        if index_temp != -1:
            self.queue[index_temp][1] = value
        # if word was not in queue
        else:
            if len(self.queue) == self.capacity:
                self.queue.sort(key=self.sort_key)
                self.queue[0] = [key, value]
            else:  # if was smaller than LENGTH
                self.queue.append([key, value])

    def __contain(self, key):
        for i in range(0, len(self.queue)):
            if self.queue[i][0] == key:
                return i
        return -1

    def is_contain(self, key):
        for i in range(0, len(self.queue)):
            if self.queue[i][0] == key:
                return True
        return False

    def sort_key(self, element):
        return element[1]
