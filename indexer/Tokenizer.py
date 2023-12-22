from PriorityQueueWithFixedLength import PriorityQueueWithFixedLength


class Tokenizer:
    def __init__(self):
        # self.stream_token = []
        pass

    def tokenize(self, document_content: list[str], document_len: int, dictionary: dict,
                 priority_queue_with_fixed_length: PriorityQueueWithFixedLength) -> None:
        for i in range(document_len):
            self.__doc_tokenize(str(i + 1), document_content[i], dictionary, priority_queue_with_fixed_length)

    def __doc_tokenize(self, doc_id: str, doc_string: str, dictionary: dict,
                       priority_queue_with_fixed_length: PriorityQueueWithFixedLength) -> None:
        word = ''
        position = 1
        for char in doc_string.strip():
            # todo: be nazaram in " or char == half_space_char " nabashe behtare
            if char == ' ' or char == '\t' or char == '\n':
                if word.strip() != '':
                    # add word to stream token
                    # self.stream_token.append((word, position, doc_id))
                    word_frequency = self.__add_to_dictionary_and_postings_list(word, doc_id, position, dictionary)
                    priority_queue_with_fixed_length.push(word, word_frequency)
                    word = ''
                    position += 1
            else:
                word += char

        if word.strip() != '':
            # self.stream_token.append((word, position, doc_id))
            word_frequency = self.__add_to_dictionary_and_postings_list(word, doc_id, position, dictionary)
            priority_queue_with_fixed_length.push(word, word_frequency)

    def __add_to_dictionary_and_postings_list(self, word: str, doc_id: str, position: int, dictionary: dict) -> int:
        # new if not exist
        if dictionary[word] is None:
            dictionary[word] = (0, {})
            dictionary[word][1][doc_id] = (0, [])

        # add to dictionary
        dictionary[word][1][doc_id][0] += 1
        dictionary[word][1][doc_id][1].append(position)
        dictionary[word][0] += 1  # increment collection frequency of word
        return dictionary[word][0]

        # if dictionary[word] is not None:
        #     dictionary[word][1][doc_id][0] += 1
        #     dictionary[word][1][doc_id][1].append(position)
        # else:
        #     dictionary[word] = (0, {})
        #     dictionary[word][1][doc_id] = (0, [])
        #     dictionary[word][1][doc_id][0] += 1
        #     dictionary[word][1][doc_id][1].append(position)
        # dictionary[word][0] += 1  # increment collection frequency of word
