from parsivar import stemmer


class Stemmer:
    def __init__(self):
        pass

    def stem(self, word):
        return stemmer.FindStems.convert_to_stem(word)
