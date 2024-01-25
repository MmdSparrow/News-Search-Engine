from parsivar.stemmer import FindStems
from hazm.stemmer import Stemmer
from hazm.word_tokenizer import WordTokenizer
from parsivar.tokenizer import Tokenizer
from index.Tokenizer import Tokenizer as MyTokenizer


def parsivar_stem(word, word_pos=None):
    return FindStems().convert_to_stem(word, word_pos)


def hazm_stem(word):
    return Stemmer().stem(word)


tokenizer = Tokenizer()

parsivarTokenizer = Tokenizer()
print(parsivarTokenizer.tokenize_words("‌خواهم رفت از این دنیا"))

hazmTokenizer = WordTokenizer()
print(hazmTokenizer.tokenize("خواهم رفت از این دنیا"))

print(hazm_stem("خواهم_رفت"))

myTokenizer = MyTokenizer()
print(myTokenizer.tokenize_query("نمی‌خواهم بروم از این دنیا"))
