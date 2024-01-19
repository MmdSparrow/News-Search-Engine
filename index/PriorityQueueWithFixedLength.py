class PriorityQueueWithFixedLength:
    LENGTH = 50

    def __init__(self, capacity: int = LENGTH):
        self.capacity = capacity
        # [key, value, index in queue]
        self.min_threshold = ['', 0]
        # we add [word, frequency] to following list
        self.queue = []

    def push(self, key, value):
        # if word was in queue update its frequency
        index_temp = self.__contain(key)
        if index_temp != -1:
            self.queue[index_temp][1] = value
            # update min
            self.__update_min_threshold()
        # if word was not in queue
        else:
            if len(self.queue) == self.capacity:
                if self.min_threshold[1] < value:
                    self.queue.sort(key=self.__sort_key)
                    self.queue[0] = [key, value]
                    # update min
                    self.__update_min_threshold()
            else:  # if was smaller than LENGTH
                self.queue.append([key, value])
                if self.min_threshold[1] > value:
                    self.min_threshold[1] = value
                    self.min_threshold[0] = key

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

    def __sort_key(self, element):
        return element[1]

    def __update_min_threshold(self):
        self.queue.sort(key=self.__sort_key)
        self.min_threshold = self.queue[0]