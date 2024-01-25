import re


class Normalizer:
    SPACE_CHARACTER = ' '
    HALF_SPACE_CHARACTER = chr(0x200c)

    def __init__(self):
        pass

    def normalize_document(self, documents_content: list, documents_content_length: int):
        for i in range(documents_content_length):
            doc = self.__delete_end_of_content(documents_content[i])
            doc = self.__remove_dots_except_emails(doc)
            doc = self.__character_delete(doc)
            doc = self.__unicode_replacement(doc)
            doc = self.__space_correction(doc)
            doc = self.__verb_prefix_separation(doc)
            doc = self.__english_digit_replacement(doc)
            documents_content[i] = self.__abbreviation_replacement(doc)

    def normalize_query(self, query: str):
        query = self.__remove_dots_except_emails(query)
        query = self.__character_delete(query)
        query = self.__unicode_replacement(query)
        query = self.__space_correction(query)
        query = self.__verb_prefix_separation(query)
        query = self.__english_digit_replacement(query)
        return self.__abbreviation_replacement(query)

    def __delete_end_of_content(self, doc_string):
        # انتهای پیام/
        return doc_string[0:len(doc_string) - 13]

    def __space_correction(self, doc_string: str):

        SPACE_POSTFIX = ['ی', 'ای', 'ها', 'های', 'هایی', 'تر', 'ترین', 'گر', 'گری', 'ام', 'ات', 'اش']
        SPACE_PREFIX = ['می', 'نمی']

        space_correction_items = {}
        for postfix in SPACE_POSTFIX:
            space_correction_items[
                self.SPACE_CHARACTER + postfix + self.SPACE_CHARACTER] = self.HALF_SPACE_CHARACTER + postfix + self.SPACE_CHARACTER

        for prefix in SPACE_PREFIX:
            space_correction_items[
                self.SPACE_CHARACTER + prefix + self.SPACE_CHARACTER] = self.SPACE_CHARACTER + prefix + self.HALF_SPACE_CHARACTER

        space_correction_items = dict((re.escape(k), v) for k, v in space_correction_items.items())
        space_correction_pattern = re.compile("|".join(space_correction_items.keys()))

        return space_correction_pattern.sub(lambda m: space_correction_items[re.escape(m.group(0))], doc_string)

    def __unicode_replacement(self, doc_string):

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

    def __character_delete(self, doc_string):
        # alef keshide bayad character ghablish fathe bashe baadesh alef biad un moghe mishe alef keshide. pas bayad ghabl az hazf fathe hazf shavad!
        CHARACTER_DELETE_KEYS = ['ْ', 'ٌ', 'ٍ', 'ً', 'ُ', 'ِ', 'َ', 'ّ', '!', '>', '<', ',', '،', 'ٰ', '؛', ':', '{',
                                 '}', '[', ']', ')', '(', '*', ';', '\"', '\'', '. ', ' .']
        CHARACTER_DELETE_VALUE = ' '  # space is better than nothing: 'cuase the writing rules may not have been followed correctly (eg. lab lab lab.lab lab lab)
        # CHARACTER_DELETE_VALUE = ''

        character_delete_item = {}
        for char in CHARACTER_DELETE_KEYS:
            character_delete_item[char] = CHARACTER_DELETE_VALUE

        character_delete_item = dict((re.escape(k), v) for k, v in character_delete_item.items())
        character_delete_pattern = re.compile("|".join(character_delete_item.keys()))

        return character_delete_pattern.sub(lambda m: character_delete_item[re.escape(m.group(0))], doc_string)

    def __remove_dots_except_emails(self, doc_string):
        email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
        email_matches = email_pattern.findall(doc_string)
        result_string = re.sub(r'\.', ' ', doc_string)
        for email in email_matches:
            result_string = result_string.replace(email.replace('.', ' '), email)

        return result_string

    def __english_digit_replacement(self, doc_string):

        ENGLISH_DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        PERSIAN_DIGITS = ['۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹']

        digit_replacement_items = {}

        for i in range(0, 10):
            digit_replacement_items[ENGLISH_DIGITS[i]] = PERSIAN_DIGITS[i]

        digit_replacement_items = dict((re.escape(k), v) for k, v in digit_replacement_items.items())
        digit_replacement_pattern = re.compile("|".join(digit_replacement_items.keys()))

        return digit_replacement_pattern.sub(lambda m: digit_replacement_items[re.escape(m.group(0))], doc_string)

    def __verb_prefix_separation(self, doc_string):
        verb_prefix_separation_items = {}
        verb_prefix_separation_items[self.SPACE_CHARACTER + 'می'] = self.SPACE_CHARACTER + 'می' + self.HALF_SPACE_CHARACTER
        verb_prefix_separation_items[self.SPACE_CHARACTER + 'نمی'] = self.SPACE_CHARACTER + 'نمی' + self.HALF_SPACE_CHARACTER

        verb_prefix_separation_items = dict((re.escape(k), v) for k, v in verb_prefix_separation_items.items())
        verb_prefix_separation_pattern = re.compile("|".join(verb_prefix_separation_items.keys()))

        return verb_prefix_separation_pattern.sub(lambda m: verb_prefix_separation_items[re.escape(m.group(0))], doc_string)

    def __abbreviation_replacement(self, doc_string):
        persian_abbreviation_dict = {}
        persian_abbreviation_dict['آجا'] = 'ارتش جمهوری اسلامی ایران'
        persian_abbreviation_dict['ناجا'] = 'نیروی انتظامی جمهوری اسلامی ایران'
        persian_abbreviation_dict['نوپو'] = 'نیروی ویژه پاد وحشت'
        persian_abbreviation_dict['پاد'] = 'پایگاه اطلاع رسانی دولت'
        persian_abbreviation_dict['آپ'] = 'آسان پرداخت'
        persian_abbreviation_dict['برجام'] = 'برنامه جامع اقدام مشترک'
        persian_abbreviation_dict['N.A.S.A'] = 'سازمان ملی هوانوردی و فضایی'
        persian_abbreviation_dict['NASA'] = 'سازمان ملی هوانوردی و فضایی'
        persian_abbreviation_dict['ناسا'] = 'سازمان ملی هوانوردی و فضایی'
        persian_abbreviation_dict['ج.ا.ا'] = 'جمهوری اسلامی ایران'
        persian_abbreviation_dict['USA'] = 'آمریکا'
        persian_abbreviation_dict['U.S.A'] = 'آمریکا'
        persian_abbreviation_dict['شبا'] = 'شماره حساب بانکی'
        persian_abbreviation_dict['ساتا'] = 'سازمان تایمن اجتماعی'
        persian_abbreviation_dict['ساتنا'] = 'سازمان تسویه ناخالص آنی'
        persian_abbreviation_dict['ساجا'] = 'سازمان ارتش جمهوری اسلامی'
        persian_abbreviation_dict['ساجب'] = 'سازمان جهانی بهداشت'
        persian_abbreviation_dict['سادا'] = 'سازمان اسلامی دانشجویان ایران'
        persian_abbreviation_dict['اتکا'] = 'اداره تدارکات کارمندان ارتش'
        abbreviation_items = {}
        for key in persian_abbreviation_dict.keys():
            abbreviation_items[self.SPACE_CHARACTER + key + self.SPACE_CHARACTER] = self.SPACE_CHARACTER + persian_abbreviation_dict[key] + self.SPACE_CHARACTER

        persian_abbreviation_dict = dict((re.escape(k), v) for k, v in persian_abbreviation_dict.items())
        persian_abbreviation_pattern = re.compile("|".join(persian_abbreviation_dict.keys()))

        return persian_abbreviation_pattern.sub(lambda m: persian_abbreviation_dict[re.escape(m.group(0))], doc_string)


