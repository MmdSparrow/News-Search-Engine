from PriorityQueueWithFixedLength import PriorityQueueWithFixedLength


class Tokenizer:
    def __init__(self):
        self.stream_token = []
        self.word_frequency_dict = {}

    def tokenize_document(self, document_content: list[str], document_len: int, priority_queue_with_fixed_length: PriorityQueueWithFixedLength) -> (list[tuple[str, str, int]], dict):
        for i in range(document_len):
            self.__doc_tokenize(str(i), document_content[i], priority_queue_with_fixed_length)
        return self.stream_token, self.word_frequency_dict

    def __doc_tokenize(self, doc_id: str, doc_string: str, priority_queue_with_fixed_length: PriorityQueueWithFixedLength) -> None:
        word = ''
        position = 1
        for char in doc_string.strip():
            # todo: be nazaram in " or char == half_space_char " nabashe behtare
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
        if self.word_frequency_dict.keys().__contains__(word):
            self.word_frequency_dict[word] += 1
        else:
            self.word_frequency_dict[word] = 1
        return self.word_frequency_dict[word]
