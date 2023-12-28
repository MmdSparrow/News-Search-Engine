from index.PriorityQueueWithFixedLength import PriorityQueueWithFixedLength
from index.CustomStemmer import CustomStemmer


class LinguisticModule:
    def __init__(self):
        self.most_repeated_word = PriorityQueueWithFixedLength()
        self.stemmer = CustomStemmer()

    def delete_50_most_repeated_words(self, dictionary: dict):
        # stem word in queue
        print('50 most repeated words:')
        for i in range(min(self.most_repeated_word.LENGTH, len(dictionary))):
            # print for report
            print(f'word: {self.most_repeated_word.queue[i][0]}')
            stem_word = self.stemmer.stem(self.most_repeated_word.queue[i][0])
            print(f'stem: {stem_word}')
            try:
                dictionary.pop(stem_word)
            except KeyError:  # if there exist two word with same stem in most repeated word list we got error in this step
                pass