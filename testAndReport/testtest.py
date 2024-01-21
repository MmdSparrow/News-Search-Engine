from index.Tokenizer import Tokenizer
from index.PriorityQueueWithFixedLength import PriorityQueueWithFixedLength
from hazm.word_tokenizer import WordTokenizer
# from hazm.
# from parsivar.tokenizer import Tokenizer

from index.Tokenizer import Tokenizer

tokenizer = Tokenizer()
priorityQueue = PriorityQueueWithFixedLength()
print(tokenizer.tokenize_query("می‌خواهم بروم از این دنیا رفته است بزرگ است"))

# parsivarTokenizer = Tokenizer()
# print(parsivarTokenizer.tokenize_words("میخواهم بروم از این دنیای کیری"))
#
#
hazmTokenizer = WordTokenizer()
print(hazmTokenizer.tokenize("می خواهم بروم از این دنیای رفته است"))
