from parsivar.stemmer import FindStems
from hazm.stemmer import Stemmer


def parsivar_stem(word, word_pos=None):
    print(FindStems().convert_to_stem(word, word_pos))

def hazm_stem(word):
     print(Stemmer().stem(word))

hazm_stem('اخبار')
hazm_stem('خبرگزاری')
hazm_stem('خبرگزار')
hazm_stem('خبرگان')
hazm_stem('اخباری')
hazm_stem('خبرنگار')
hazm_stem('خبرنگاری')
hazm_stem('مسابفات')


