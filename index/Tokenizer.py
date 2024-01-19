from index.PriorityQueueWithFixedLength import PriorityQueueWithFixedLength
from pathlib import Path


class Tokenizer:
    HALF_SPACE_CHARACTER = chr(0x200c)
    SPACE_CHARACTER = ' '

    def __init__(self):
        self.stream_token = []
        self.word_frequency_dict = {}
        self.special_word_for_halfspace_separation = ['می‌', 'می']
        self.exception_for_before_verbs = {'که', 'به', 'در', 'از', 'با', 'بر'}
        with Path.open(Path("../data/verbs.dat"), encoding="utf8") as verbs_file:
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
            "شده‌ام",
            "شده‌ای",
            "شده‌است",
            "شده‌ایم",
            "شده‌اید",
            "شده‌اند",
            "شده‌بودم",
            "شده‌بودی",
            "شده‌بود",
            "شده‌بودیم",
            "شده‌بودید",
            "شده‌بودند",
            "شده‌باشم",
            "شده‌باشی",
            "شده‌باشد",
            "شده‌باشیم",
            "شده‌باشید",
            "شده‌باشند",
            "نشده‌ام",
            "نشده‌ای",
            "نشده‌است",
            "نشده‌ایم",
            "نشده‌اید",
            "نشده‌اند",
            "نشده‌بودم",
            "نشده‌بودی",
            "نشده‌بود",
            "نشده‌بودیم",
            "نشده‌بودید",
            "نشده‌بودند",
            "نشده‌باشم",
            "نشده‌باشی",
            "نشده‌باشد",
            "نشده‌باشیم",
            "نشده‌باشید",
            "نشده‌باشند",
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
            "خواهم‌شد",
            "خواهی‌شد",
            "خواهد‌شد",
            "خواهیم‌شد",
            "خواهید‌شد",
            "خواهند‌شد",
            "نخواهم‌شد",
            "نخواهی‌شد",
            "نخواهد‌شد",
            "نخواهیم‌شد",
            "نخواهید‌شد",
            "نخواهند‌شد",
        }

    def tokenize_document(self, document_content: list[str], document_len: int, priority_queue_with_fixed_length: PriorityQueueWithFixedLength) -> (
            list[tuple[str, str, int]], dict):
        for i in range(document_len):
            self.__doc_tokenize(str(i), document_content[i], priority_queue_with_fixed_length)
        # post process
        self.__postProcessTokenStream()
        return self.stream_token

    def __doc_tokenize(self, doc_id: str, doc_string: str, priority_queue_with_fixed_length: PriorityQueueWithFixedLength) -> None:
        word = ''
        position = 1
        for char in doc_string.strip():
            # todo: be nazaram in " or char == half_space_char " nabashe behtare
            # if char == ' ' or char == '\t' or char == '\n' or (char == self.HALF_SPACE_CHARACTER and (word in self.special_word_for_halfspace_separation)):
            if char == ' ' or char == '\t' or char == '\n':
                word = word.strip()
                if word != '':
                    # add word to stream token
                    self.stream_token.append((word, doc_id, position))
                    word_frequency = self.__update_frequency(word)
                    priority_queue_with_fixed_length.push(word, word_frequency)
                    word = ''
                    position += 1
            else:
                word += char

        if word.strip() != '':
            self.stream_token.append((word, position, doc_id))
            word_frequency = self.__update_frequency(word)
            priority_queue_with_fixed_length.push(word, word_frequency)

    def __update_frequency(self, word: str) -> int:
        if word in self.word_frequency_dict:
            self.word_frequency_dict[word] = self.word_frequency_dict[word] + 1
        else:
            self.word_frequency_dict[word] = 1
        return self.word_frequency_dict[word]

    def __postProcessTokenStream(self):
        # before verbs
        for i in range(len(self.stream_token) - 1):
            if self.stream_token[i] is not None and self.stream_token[i + 1] is not None:
                if self.stream_token[i][0] in self.before_verbs and self.stream_token[i + 1][0] not in self.exception_for_before_verbs:
                    self.stream_token[i] = (self.stream_token[i][0] + self.SPACE_CHARACTER + self.stream_token[i + 1][0], self.stream_token[i][1], self.stream_token[i][2])
                    i += 1
                    self.stream_token[i] = None

        # after verb
        for i in range(len(self.stream_token) - 1):
            if self.stream_token[i] is not None and self.stream_token[i + 1] is not None:
                if self.stream_token[i][0] in self.verbe and self.stream_token[i + 1][0] in self.after_verbs:
                    self.stream_token[i] = (self.stream_token[i][0] + self.HALF_SPACE_CHARACTER + self.stream_token[i + 1][0], self.stream_token[i][1], self.stream_token[i][2])
                    i += 1
                    self.stream_token[i] = None
