from PriorityQueueWithFixedLength import PriorityQueueWithFixedLength
from CustomStemmer import CustomStemmer


class Tokenizer:
    def __init__(self):
        # self.stream_token = []
        pass

    def tokenize(self, document_content: list[str], document_len: int, dictionary: dict,
                 priority_queue_with_fixed_length: PriorityQueueWithFixedLength, stemmer: CustomStemmer) -> None:
        for i in range(document_len):
            # todo: doc id nabayad az yek shoro beshe
            # self.__doc_tokenize(str(i + 1), document_content[i], dictionary, priority_queue_with_fixed_length, stemmer)
            self.__doc_tokenize(str(i), document_content[i], dictionary, priority_queue_with_fixed_length, stemmer)

    def __doc_tokenize(self, doc_id: str, doc_string: str, dictionary: dict,
                       priority_queue_with_fixed_length: PriorityQueueWithFixedLength, stemmer: CustomStemmer) -> None:
        word = ''
        position = 1
        for char in doc_string.strip():
            # todo: be nazaram in " or char == half_space_char " nabashe behtare
            if char == ' ' or char == '\t' or char == '\n':
                word = word.strip()
                if word != '':
                    # add word to stream token
                    word = stemmer.stem(word)
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
        # guid:
        # dictionary[word][0]: collection frequency
        # dictionary[word][1]: dictionary of docs
        # dictionary[word][1][doc_it][0]: document frequency
        # dictionary[word][1][doc_it][1]: positions

        # if dictionary not contain the word
        # i used list instead of tuple because tuple is mutable
        if not dictionary.keys().__contains__(word):
            dictionary[word] = [0, {}]
            # if dictionary not contain the doc_id
            if not dictionary[word][1].__contains__(doc_id):
                dictionary[word][1][doc_id] = [0, []]

        # add to dictionary
        dictionary[word][0] += 1  # increment collection frequency of word
        dictionary[word][0][doc_id][0] += 1  # increment document frequency of doc and word
        dictionary[word][1][doc_id][1].append(position)  # add position
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
