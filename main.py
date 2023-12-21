from preProcess.tokenizer import doc_tokenize
from re import sub
import re

s = "تست می کنم این را تست  نیم‌فاصله"
print(doc_tokenize(1, s))


def tokenize_words(doc_string):
    token_list = doc_string.strip().split()
    token_list = [x.strip("\u200c") for x in token_list if len(x.strip("\u200c")) != 0]
    return token_list


print(tokenize_words(s))


def norm(s):
    a0 = 'می' + " "
    b0 = 'می' + "\u200c"
    return s.replace(a0, b0)


print('test')
print(norm(s))


class DocumentNormalization:
    def __init__(self):
        self.space_character = ' '
        self.half_space_character = chr(0x200c)
        SPACE_POSTFIX = ['ی', 'ای ', 'ها', 'های', 'هایی', 'تر', 'ترین', 'گر', 'گری', 'ام', 'ات', 'اش']
        SPACE_PREFIX = ['می', 'نمی']

        self.space_correction_items = {}
        for postfix in SPACE_POSTFIX:
            self.space_correction_items[self.space_character + postfix + self.space_character] = self.half_space_character + postfix
        for prefix in SPACE_PREFIX:
            self.space_correction_items[self.space_character + prefix + self.space_character] = self.space_character+ prefix + self.half_space_character

        self.space_correction_items = dict((re.escape(k), v) for k, v in self.space_correction_items.items())
        self.space_correction_pattern = re.compile("|".join(self.space_correction_items.keys()))

        text = "تست می کنم این را تست  نیم‌فاصله"

        text = self.space_correction_pattern.sub(lambda m: self.space_correction_items[re.escape(m.group(0))], text)
        print(text)

print('1111111111111111111')
d = DocumentNormalization()
print('11111111111111111111111111111')
