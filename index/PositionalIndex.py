from index.LinguisticModule import LinguisticModule
from preProcess.PreProcessor import PreProcessor
from index.Tokenizer import Tokenizer


class PositionalIndex:
    def __init__(self):
        self.dictionary = {}
        self.document_length = 0
        self.documents_title_url_dict = {}

        # example
        # self.dictionary['w1'] = (0, dic)
        # self.dictionary['w1'][1][0][1].append()

    # this method sort indexes

    def create(self):
        # pre process documents
        preProcess = PreProcessor()
        self.document_length, document_content, self.documents_title_url_dict = preProcess.document_preprocessor_handler()
        print("pre processing.....................................................................done")

        # create index
        tokenizer = Tokenizer()
        linguistic_module = LinguisticModule()

        stream_token, word_frequency_dict = tokenizer.tokenize_document(document_content, self.document_length, linguistic_module.most_repeated_word)
        print("tokenizing.....................................................................done")

        linguistic_module.delete_50_most_repeated_words(word_frequency_dict)
        print("delete 50 most repeated.....................................................................done")

        # stemming was implemented in index creation phase
        self.__create_dict(stream_token, word_frequency_dict, linguistic_module.stemmer)

    def __create_dict(self, stream_token, word_frequency_dict, stemmer):
        for word, doc_id, position in stream_token:
            if word_frequency_dict.keys().__contains__(word):
                word_new = stemmer.stem(word)
                self.__add_to_dictionary_and_postings_list(word_new, doc_id, position)

    def __add_to_dictionary_and_postings_list(self, word: str, doc_id: str, position: int) -> None:
        if not self.dictionary.keys().__contains__(word):
            # [collection term frequency, document frequency (df_t), list of doc id]
            self.dictionary[word] = [0, 0, {}]
        # if dictionary not contain the doc_id:
        # increment df
        if not self.dictionary[word][2].__contains__(doc_id):
            self.dictionary[word][1] += 1
            # [document term frequency, tf-idf, positions]
            self.dictionary[word][2][doc_id] = [0, -1, []]

        # add to dictionary
        self.dictionary[word][0] += 1  # increment collection frequency of word
        self.dictionary[word][2][doc_id][0] += 1  # increment document frequency of doc and word
        self.dictionary[word][2][doc_id][2].append(position)  # add position

# test
# positional_index = PositionalIndex()
# positional_index.create()
# print(positional_index.dictionary)
