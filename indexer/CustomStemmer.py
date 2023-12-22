from hazm import Stemmer


class CustomStemmer:
    def __init__(self):
        pass

    def stem(self, word):
        return Stemmer().stem(word)
