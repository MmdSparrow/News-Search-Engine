from LinguisticModule import LinguisticModule
from preProcess.PreProcessor import PreProcessor
from Tokenizer import Tokenizer


class PositionalIndex:
    def __init__(self):
        self.dictionary = {}
        # example
        # self.dictionary['w1'] = (0, dic)
        # self.dictionary['w1'][1][0][1].append()

    # this method sort indexes

    def handler(self):
        # pre process documents
        preProcess = PreProcessor()
        document_length, document_content = preProcess.handler()

        # create index
        tokenizer = Tokenizer()
        linguistic_module = LinguisticModule()

        stream_token, word_frequency_dict = tokenizer.tokenize(document_content, document_length, linguistic_module.most_repeated_word)

        linguistic_module.delete_50_most_repeated_words(word_frequency_dict)

        # stemming was implemented in index creation phase
        self.__create(stream_token, word_frequency_dict, linguistic_module.stemmer)

    def __create(self, stream_token, word_frequency_dict, stemmer):
        for word, doc_id, position in stream_token:
            if word_frequency_dict.keys().__contains__(word):
                word_new = stemmer.stem(word)
                self.__add_to_dictionary_and_postings_list(word_new, doc_id, position)

    def __add_to_dictionary_and_postings_list(self, word: str, doc_id: str, position: int) -> None:
        if not self.dictionary.keys().__contains__(word):
            self.dictionary[word] = [0, {}]
        # if dictionary not contain the doc_id
        if not self.dictionary[word][1].__contains__(doc_id):
            self.dictionary[word][1][doc_id] = [0, []]

        # add to dictionary
        self.dictionary[word][0] += 1  # increment collection frequency of word
        self.dictionary[word][1][doc_id][0] += 1  # increment document frequency of doc and word
        self.dictionary[word][1][doc_id][1].append(position)  # add position


positional_index = PositionalIndex()
positional_index.handler()
print(positional_index.dictionary)
