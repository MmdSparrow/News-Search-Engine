from PriorityQueueWithFixedLength import PriorityQueueWithFixedLength
from parsivar import stemmer

class LinguisticModule:
    def __init__(self):
        self.most_repeated_word = PriorityQueueWithFixedLength()

    def delete_50_most_repeated_words(self, dictionary: dict):
        for i in range(self.most_repeated_word.LENGTH):
            dictionary.pop(self.most_repeated_word.queue[i])

    def stemming(self, dictionary: dict):

        stemmer.FindStems().convert_to_stem()
