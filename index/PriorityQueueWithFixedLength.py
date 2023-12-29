class PriorityQueueWithFixedLength:
    LENGTH = 50

    def __init__(self):
        # (word, frequency)
        self.queue = []

    def push(self, word, frequency):
        # if word was in queue update it's frequency
        index_temp = self.contain(word)
        if index_temp != -1:
            self.queue[index_temp][1] = frequency
        # if word was not in queue
        else:
            if len(self.queue) == self.LENGTH:
                self.queue.sort(key=self.sort_key)
                self.queue[0] = [word, frequency]
            else: # if was smaller than LENGTH
                self.queue.append([word, frequency])

    def contain(self, item):
        for i in range(0, len(self.queue)):
            if self.queue[i][0] == item:
                return i
        return -1

    def sort_key(self, element):
        return element[1]
