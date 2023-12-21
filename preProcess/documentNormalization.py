import re

SPACE_CHARACTER = ' '
HALF_SPACE_CHARACTER = chr(0x200c)


class DocumentNormalization:
    def __init__(self):
        pass

    def normalize(self, doc) -> str:
        doc = self.space_correction(doc)
        doc = self.unicode_replacement(doc)
        doc = self.character_delete(doc)
        doc = self.english_digit_replacement(doc)
        doc = self.space_correction(doc)
        return doc

    def space_correction(self, doc_string: str):

        SPACE_POSTFIX = ['ی', 'ای', 'ها', 'های', 'هایی', 'تر', 'ترین', 'گر', 'گری', 'ام', 'ات', 'اش']
        SPACE_PREFIX = ['می', 'نمی']

        space_correction_items = {}
        for postfix in SPACE_POSTFIX:
            space_correction_items[SPACE_CHARACTER + postfix + SPACE_CHARACTER] = HALF_SPACE_CHARACTER + postfix

        for prefix in SPACE_PREFIX:
            space_correction_items[
                SPACE_CHARACTER + prefix + SPACE_CHARACTER] = SPACE_CHARACTER + prefix + HALF_SPACE_CHARACTER

        space_correction_items = dict((re.escape(k), v) for k, v in space_correction_items.items())
        space_correction_pattern = re.compile("|".join(space_correction_items.keys()))

        return space_correction_pattern.sub(lambda m: space_correction_items[re.escape(m.group(0))], doc_string)

    def unicode_replacement(self, doc_string):

        unicode_replacement_items = {}

        # char...............
        ALFE1_CHARACTER_KEYS = ['أ', 'ﺍ', 'إ', 'ٱ', 'ٲ']
        ALEF1_CHARACTER_VALUE = "ا"
        for char in ALFE1_CHARACTER_KEYS:
            unicode_replacement_items[char] = ALEF1_CHARACTER_VALUE

        ALFE2_CHARACTER_KEYS = ['آ', 'ﺁ']
        ALEF2_CHARACTER_VALUE = "آ"
        for char in ALFE2_CHARACTER_KEYS:
            unicode_replacement_items[char] = ALEF2_CHARACTER_VALUE

        BE_CHARACTER_KEYS = ['ي', 'ى', 'ے', 'ێ', 'ﯿ', 'ﯾ', 'ﯽ', 'ې', 'ﯼ', 'ﻴ', 'ﻳ', 'ں', 'ﻲ', 'ﻱ', 'ﻰ', 'ۍ', 'ﻯ', 'ﭛ']
        BE_CHARACTER_VALUE = "ی"
        for char in BE_CHARACTER_KEYS:
            unicode_replacement_items[char] = BE_CHARACTER_VALUE

        KAF_CHARACTER_KEYS = ['ك', 'ڪ', 'ﮐ', 'ﮑ', 'ﻛ', 'ګ', 'ﮏ', 'ﻜ', 'ﮎ', 'ﻚ', 'ڭ']
        KAF_CHARACTER_VALUE = "ک"
        for char in KAF_CHARACTER_KEYS:
            unicode_replacement_items[char] = KAF_CHARACTER_VALUE

        # word...............
        unicode_replacement_items['طهران'] = 'تهران'
        unicode_replacement_items['بلیط'] = 'بلیت'
        unicode_replacement_items['باطلاق'] = 'باتلاق'
        unicode_replacement_items['هيأت'] = 'هيئت'
        unicode_replacement_items['طوسي'] = 'توسي'
        unicode_replacement_items['تزيين'] = 'تزئين'
        unicode_replacement_items['رییس'] = 'رئیس'
        unicode_replacement_items['اطاق'] = 'اتاق'
        unicode_replacement_items['اصطبل'] = 'اسطبل'
        unicode_replacement_items['باطری'] = 'باتری'
        unicode_replacement_items['توفان'] = 'طوفان'
        unicode_replacement_items['بغچه'] = 'بقچه'

        unicode_replacement_items = dict((re.escape(k), v) for k, v in unicode_replacement_items.items())
        unicode_replacement_pattern = re.compile("|".join(unicode_replacement_items.keys()))

        return unicode_replacement_pattern.sub(lambda m: unicode_replacement_items[re.escape(m.group(0))], doc_string)

    def character_delete(self, doc_string):
        #todo:
        character_delete_keys = []
        character_delete_value = ''
        return doc_string

    def english_digit_replacement(self, doc_string):

        ENGLSIH_DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        PERSIAN_DIGITS = ['۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹']

        digit_replacement_items = {}

        for i in range(0, 10):
            digit_replacement_items[ENGLSIH_DIGITS[i]] = PERSIAN_DIGITS[i]

        digit_replacement_items = dict((re.escape(k), v) for k, v in digit_replacement_items.items())
        digit_replacement_pattern = re.compile("|".join(digit_replacement_items.keys()))

        return digit_replacement_pattern.sub(lambda m: digit_replacement_items[re.escape(m.group(0))], doc_string)

    def verb_prefix_separation(self, doc_string):
        #todo:
        return doc_string
