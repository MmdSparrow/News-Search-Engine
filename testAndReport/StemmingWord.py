from parsivar.stemmer import FindStems
from hazm.stemmer import Stemmer


def parsivar_stem(word, word_pos=None):
    return FindStems().convert_to_stem(word, word_pos)

def hazm_stem(word):
    return Stemmer().stem(word)

hazm_stem('خبرگزاری')
hazm_stem('خبرگان')
hazm_stem('اخبار')