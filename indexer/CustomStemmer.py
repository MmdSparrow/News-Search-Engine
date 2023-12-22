# from hazm import Stemmer
from parsivar.stemmer import FindStems

class CustomStemmer:
    def __init__(self):
        pass

    # def stem(self, word):
    #     return Stemmer().stem(word)

    # parsivar
    def stem(self, word, word_pos=None):
        return FindStems().convert_to_stem(word, word_pos)
