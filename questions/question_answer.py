# چون {می خواهد برود} توسط هیچ یک از stemizer های کتابخانه های پینهاد شده ساپورت نمی شود پس باید آن ها را دوتا توکن جدا در نظر بگیریم

from parsivar.stemmer import FindStems
from hazm.stemmer import Stemmer


def parsivar_stem(word, word_pos=None):
    return FindStems().convert_to_stem(word, word_pos)

def hazm_stem(word):
    return Stemmer().stem(word)

print('parsiavr:')
print(parsivar_stem('می خواهد'))
print(parsivar_stem('میخواهد'))
print(parsivar_stem('میخواهد برود'))
print()
print('hazm:')
print(hazm_stem('می خواهد'))
print(hazm_stem('میخواهد'))
print(hazm_stem('میخواهد برود'))