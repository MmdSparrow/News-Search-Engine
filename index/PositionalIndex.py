from index.LinguisticModule import LinguisticModule
from preProcess.PreProcessor import PreProcessor
from index.Tokenizer import Tokenizer
import datetime


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

        stream_token = tokenizer.tokenize_document(document_content, self.document_length, linguistic_module.most_repeated_word)
        print(f"tokenizing.....................................................................done")

        start_time = datetime.datetime.now()
        stream_token = linguistic_module.delete_50_most_repeated_words_stem_remains_from_tokens(stream_token)
        print("delete 50 most repeated.....................................................................done")
        end_time = datetime.datetime.now()
        print("time elapsed: ", end_time - start_time)

        start_time = datetime.datetime.now()
        # stemming was implemented in index creation phase
        self.__create_dict(stream_token)
        end_time = datetime.datetime.now()
        print("time elapsed: ", end_time - start_time)

    def __create_dict(self, stream_token):
        for word, doc_id, position in stream_token:
            self.__add_to_dictionary_and_postings_list(word, doc_id, position)

    def __add_to_dictionary_and_postings_list(self, word: str, doc_id: str, position: int) -> None:
        if word not in self.dictionary:
            # [collection term frequency, document frequency (df_t), list of doc id]
            self.dictionary[word] = [0, 0, {}]
        # if dictionary not contain the doc_id:
        # increment df
        if doc_id not in self.dictionary[word][2]:
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
