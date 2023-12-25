from indexer.PriorityQueueWithFixedLength import PriorityQueueWithFixedLength
from indexer.CustomStemmer import CustomStemmer


class LinguisticModule:
    def __init__(self):
        self.most_repeated_word = PriorityQueueWithFixedLength()
        self.stemmer = CustomStemmer()

    def delete_50_most_repeated_words(self, dictionary: dict):
        for i in range(min(self.most_repeated_word.LENGTH, len(dictionary))):
            dictionary.pop(self.most_repeated_word.queue[i][0])
