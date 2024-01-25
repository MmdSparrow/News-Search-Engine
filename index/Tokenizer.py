import regex as re
from pathlib import Path
from index.PriorityQueueWithFixedLength import PriorityQueueWithFixedLength


class Tokenizer:
    HALF_SPACE_CHARACTER = chr(0x200c)
    ZERO_WITH_CHARACTER = "\u8204"
    SPACE_CHARACTER = ' '

    def __init__(self):
        self.stream_token = []
        self.word_frequency_dict = {}
        self.before_expected_word_for_halfspace_separation = ['نمی‌', 'می‌']
        self.after_expected_word_for_halfspace_separation = ['ی', 'ها', 'تر', 'گر', 'ام', 'ات', 'اش', 'های', 'تری',
                                                             'گری', 'هایی', 'ترین', 'اعداد']
        self.exception_for_before_verbs = {'که', 'به', 'در', 'از', 'با', 'بر', 'و', 'این', 'اما', 'اینکه'}
        with Path.open(Path("./data/verbs.dat"), encoding="utf8") as verbs_file:
            self.verbs = list(
                reversed([verb.strip() for verb in verbs_file if verb]),
            )
            self.bons = {verb.split("#")[0] for verb in self.verbs}
            self.verbe = set(
                [bon + "ه" for bon in self.bons]
                + ["ن" + bon + "ه" for bon in self.bons],
            )
        self.before_verbs = {
            "خواهم",
            "خواهی",
            "خواهد",
            "خواهیم",
            "خواهید",
            "خواهند",
            "نخواهم",
            "نخواهی",
            "نخواهد",
            "نخواهیم",
            "نخواهید",
            "نخواهند",

            "می‌خواهم",
            "می‌خواهی",
            "می‌خواهد",
            "می‌خواهیم",
            "می‌خواهید",
            "می‌خواهند",
            "نمی‌خواهم",
            "نمی‌خواهی",
            "نمی‌خواهد",
            "نمی‌خواهیم",
            "نمی‌خواهید",
            "نمی‌خواهند",

            "خواستم",
            "خواستی",
            "خواست",
            "خواستیم",
            "خواستید",
            "خواستند",
            "نخواستم",
            "نخواستی",
            "نخواست",
            "نخواستیم",
            "نخواستید",
            "نخواستند",

            "می‌خواستم",
            "می‌خواستی",
            "می‌خواست",
            "می‌خواستیم",
            "می‌خواستید",
            "می‌خواستند",
            "نمی‌خواستم",
            "نمی‌خواستی",
            "نمی‌خواست",
            "نمی‌خواستیم",
            "نمی‌خواستید",
            "نمی‌خواستند",

            "داشتم",
            "داشتی",
            "داشت",
            "داشتیم",
            "داشتید",
            "داشنتد",
            "دارم",
            "داری",
            "دارد",
            "داریم",
            "دارید",
            "دارند",
        }
        self.after_verbs = {
            "ام",
            "ای",
            "است",
            "ایم",
            "اید",
            "اند",
            "بودم",
            "بودی",
            "بود",
            "بودیم",
            "بودید",
            "بودند",
            "باشم",
            "باشی",
            "باشد",
            "باشیم",
            "باشید",
            "باشند",
            "شده_ام",
            "شده_ای",
            "شده_است",
            "شده_ایم",
            "شده_اید",
            "شده_اند",
            "شده_بودم",
            "شده_بودی",
            "شده_بود",
            "شده_بودیم",
            "شده_بودید",
            "شده_بودند",
            "شده_باشم",
            "شده_باشی",
            "شده_باشد",
            "شده_باشیم",
            "شده_باشید",
            "شده_باشند",
            "نشده_ام",
            "نشده_ای",
            "نشده_است",
            "نشده_ایم",
            "نشده_اید",
            "نشده_اند",
            "نشده_بودم",
            "نشده_بودی",
            "نشده_بود",
            "نشده_بودیم",
            "نشده_بودید",
            "نشده_بودند",
            "نشده_باشم",
            "نشده_باشی",
            "نشده_باشد",
            "نشده_باشیم",
            "نشده_باشید",
            "نشده_باشند",
            "شوم",
            "شوی",
            "شود",
            "شویم",
            "شوید",
            "شوند",
            "شدم",
            "شدی",
            "شد",
            "شدیم",
            "شدید",
            "شدند",
            "نشوم",
            "نشوی",
            "نشود",
            "نشویم",
            "نشوید",
            "نشوند",
            "نشدم",
            "نشدی",
            "نشد",
            "نشدیم",
            "نشدید",
            "نشدند",
            "می‌شوم",
            "می‌شوی",
            "می‌شود",
            "می‌شویم",
            "می‌شوید",
            "می‌شوند",
            "می‌شدم",
            "می‌شدی",
            "می‌شد",
            "می‌شدیم",
            "می‌شدید",
            "می‌شدند",
            "نمی‌شوم",
            "نمی‌شوی",
            "نمی‌شود",
            "نمی‌شویم",
            "نمی‌شوید",
            "نمی‌شوند",
            "نمی‌شدم",
            "نمی‌شدی",
            "نمی‌شد",
            "نمی‌شدیم",
            "نمی‌شدید",
            "نمی‌شدند",
            "خواهم_شد",
            "خواهی_شد",
            "خواهد_شد",
            "خواهیم_شد",
            "خواهید_شد",
            "خواهند_شد",
            "نخواهم_شد",
            "نخواهی_شد",
            "نخواهد_شد",
            "نخواهیم_شد",
            "نخواهید_شد",
            "نخواهند_شد",
        }

    def tokenize_document(self, document_content: list[str], document_len: int) -> (list[tuple[str, str, int]], dict):
        priority_queue_with_fixed_length = PriorityQueueWithFixedLength()
        for i in range(document_len):
            self.__doc_tokenize(str(i), document_content[i], priority_queue_with_fixed_length)
        # return self.stream_token, priority_queue_with_fixed_length

        # post process
        self.__post_process_token_stream()
        priority_queue_with_fixed_length = self.__update_queue_when_using_after_before_verbs()
        self.__persian_digit_replacement_in_id_and_email()
        return self.stream_token, priority_queue_with_fixed_length

    def __doc_tokenize(self, doc_id: str, doc_string: str,
                       priority_queue_with_fixed_length: PriorityQueueWithFixedLength) -> None:
        result = re.split('\s+', doc_string)
        result = list(filter('‌'.__ne__, result))
        final_result = []
        # before_conditions_string = ""
        # after_conditions_string = self.after_expected_word_for_halfspace_separation[0]
        # for i_str in self.before_expected_word_for_halfspace_separation:
        #     before_conditions_string += "(?<!" + i_str + ')'
        # for i in range(1, len(self.after_expected_word_for_halfspace_separation)):
        #     after_conditions_string += " |" + self.after_expected_word_for_halfspace_separation[i]
        regex_str = r'(?<!می)(?<!نمی)(' + self.ZERO_WITH_CHARACTER + "|" + self.HALF_SPACE_CHARACTER + ')+(?!ی)(?!ها)(?!تر)(?!گر)(?!ام)(?!اش)(?!های)(?!تری)(?!گری)(?!هایی)(?!ترین)(?!اعداد)'
        for word in result:
            final_result.extend(re.split(regex_str, self.__multiple_half_space_replacer(word)))

        final_result = list(filter(''.__ne__, final_result))
        final_result = list(filter('‌'.__ne__, final_result))


        position = 1
        for word in final_result:
            self.stream_token.append((word, doc_id, position))
            word_frequency = self.__update_frequency(word)
            priority_queue_with_fixed_length.push(word, word_frequency)
            position += 1

    def __update_frequency(self, word: str) -> int:
        if word in self.word_frequency_dict:
            self.word_frequency_dict[word] = self.word_frequency_dict[word] + 1
        else:
            self.word_frequency_dict[word] = 1
        return self.word_frequency_dict[word]

    def __post_process_token_stream(self):
        # before verbs
        for i in range(len(self.stream_token) - 1):
            if self.stream_token[i] is not None and self.stream_token[i + 1] is not None and self.stream_token[i][1] == \
                    self.stream_token[i + 1][1]:
                if self.stream_token[i][0] in self.before_verbs and self.stream_token[i + 1][
                    0] not in self.exception_for_before_verbs:
                    self.stream_token[i] = (
                    self.stream_token[i][0] + "_" + self.stream_token[i + 1][0], self.stream_token[i][1],
                    self.stream_token[i][2])
                    i += 1
                    self.stream_token[i] = None

        # after verb
        for i in range(len(self.stream_token) - 1):
            if self.stream_token[i] is not None and self.stream_token[i + 1] is not None and self.stream_token[i][1] == \
                    self.stream_token[i + 1][1]:
                if self.stream_token[i][0] in self.verbe and self.stream_token[i + 1][0] in self.after_verbs:
                    self.stream_token[i] = (
                    self.stream_token[i][0] + "_" + self.stream_token[i + 1][0], self.stream_token[i][1],
                    self.stream_token[i][2])
                    i += 1
                    self.stream_token[i] = None

        self.stream_token = list(filter(None, self.stream_token))

    def __update_queue_when_using_after_before_verbs(self):
        new_queue = PriorityQueueWithFixedLength()
        new_word_frequency_dict = {}

        for token in self.stream_token:
            if token[0] not in new_word_frequency_dict:
                new_word_frequency_dict[token[0]] = 1
            else:
                new_word_frequency_dict[token[0]] += 1
            new_queue.push(token[0], new_word_frequency_dict[token[0]])

        return new_queue

    def tokenize_query(self, query_string):
        result = re.split('\s+', query_string)
        final_result = []
        # before_conditions_string = ""
        # after_conditions_string = self.after_expected_word_for_halfspace_separation[0]
        # for i_str in self.before_expected_word_for_halfspace_separation:
        #     before_conditions_string += "(?<!" + i_str + ')'
        # for i in range(1, len(self.after_expected_word_for_halfspace_separation)):
        #     after_conditions_string += " |" + self.after_expected_word_for_halfspace_separation[i]
        regex_str = r'(?<!می)(?<!نمی)(' + self.ZERO_WITH_CHARACTER + "|" + self.HALF_SPACE_CHARACTER + ')+(?!ی)(?!ها)(?!تر)(?!گر)(?!ام)(?!اش)(?!های)(?!تری)(?!گری)(?!هایی)(?!ترین)(?!اعداد)'
        for word in result:
            final_result.extend(re.split(regex_str, self.__multiple_half_space_replacer(word)))

        final_result = list(filter(''.__ne__, final_result))

        position = 1
        query_tokens = []
        for word in final_result:
            query_tokens.append((word, position))
            position += 1

        # before verbs
        for i in range(len(query_tokens) - 1):
            if query_tokens[i] is not None and query_tokens[i + 1] is not None:
                if query_tokens[i][0] in self.before_verbs and query_tokens[i + 1][
                    0] not in self.exception_for_before_verbs:
                    query_tokens[i] = (query_tokens[i][0] + "_" + query_tokens[i + 1][0], query_tokens[i][1])
                    i += 1
                    query_tokens[i] = None

        # after verb
        for i in range(len(query_tokens) - 1):
            if query_tokens[i] is not None and query_tokens[i + 1] is not None:
                if query_tokens[i][0] in self.verbe and query_tokens[i + 1][0] in self.after_verbs:
                    query_tokens[i] = (query_tokens[i][0] + "_" + query_tokens[i + 1][0], query_tokens[i][1])
                    i += 1
                    query_tokens[i] = None

        query_tokens = list(filter(None, query_tokens))

        PERSIAN_DIGITS = ['۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹']
        ENGLISH_DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        digit_replacement_items = {}

        for i in range(0, 10):
            digit_replacement_items[PERSIAN_DIGITS[i]] = ENGLISH_DIGITS[i]

        digit_replacement_items = dict((re.escape(k), v) for k, v in digit_replacement_items.items())
        digit_replacement_pattern = re.compile("|".join(digit_replacement_items.keys()))
        for i in range(len(query_tokens)):
            if '@' in query_tokens[i][0]:
                query_tokens[i] = (
                    digit_replacement_pattern.sub(lambda m: digit_replacement_items[re.escape(m.group(0))],
                                                  query_tokens[i][0]),
                    query_tokens[i][1]
                )

        token_frequency = {}
        for token in query_tokens:
            if token[0] in token_frequency:
                token_frequency[token[0]] += 1
            else:
                token_frequency[token[0]] = 1

        # word: frequency, list of positions
        stream_query_tokens = {}
        for token in query_tokens:
            if token[0] in stream_query_tokens:
                stream_query_tokens[token[0]][1].append(token[1])
                stream_query_tokens[token[0]][0] += 1
            else:
                stream_query_tokens[token[0]] = [1, [token[1]]]

        return stream_query_tokens

    def __persian_digit_replacement_in_id_and_email(self):

        PERSIAN_DIGITS = ['۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹']
        ENGLISH_DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        digit_replacement_items = {}

        for i in range(0, 10):
            digit_replacement_items[PERSIAN_DIGITS[i]] = ENGLISH_DIGITS[i]

        digit_replacement_items = dict((re.escape(k), v) for k, v in digit_replacement_items.items())
        digit_replacement_pattern = re.compile("|".join(digit_replacement_items.keys()))
        for i in range(len(self.stream_token)):
            if '@' in self.stream_token[i][0]:
                self.stream_token[i] = (
                    digit_replacement_pattern.sub(lambda m: digit_replacement_items[re.escape(m.group(0))],
                                                  self.stream_token[i][0]),
                    self.stream_token[i][1],
                    self.stream_token[i][2]
                )

    def __multiple_half_space_replacer(self, word):
        word = word.replace('‌‌', '‌')
        word = word.replace('‌‌', '‌')
        word = word.replace('‌‌', '‌')
        word = word.replace('‌‌', '‌')
        return word
