from index.LinguisticModule import LinguisticModule
from preProcess.PreProcessor import PreProcessor
from index.Tokenizer import Tokenizer
from index.Index import Index
from index.Postings import Postings
from index.PriorityQueueWithFixedLength import PriorityQueueWithFixedLength
from index.CustomStemmer import CustomStemmer


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

        # stemming was implemented in index creation phase
        self.__create_dict(stream_token, linguistic_module.stemmer, linguistic_module.most_repeated_word)
        print("creating dictionary.....................................................................done")
        print("delete 50 most repeated.....................................................................done")

        # delete most frequent token
        # linguistic_module.delete_50_most_repeated_words(self.dictionary)
        # print("delete 50 most repeated.....................................................................done")

    def __create_dict(self, stream_token, stemmer: CustomStemmer, most_repeated_word_queue: PriorityQueueWithFixedLength):
        # create the indices
        df, tf, i = 0, 0, 0
        while i < len(stream_token):
            index = Index()
            last_term = stream_token[i][0]
            while i < len(stream_token) and stream_token[i][0] == last_term:
                last_id = stream_token[i][1]
                postings = Postings(last_id)
                while i < len(stream_token) and stream_token[i][0] == last_term and stream_token[i][1] == last_id:
                    postings.add_posting(stream_token[i][2])
                    i += 1
                index.add_postings(postings)
            if most_repeated_word_queue.contain(last_term):
                self.dictionary[stemmer.stem(last_term)] = index

# test
# positional_index = PositionalIndex()
# positional_index.create()
# print(positional_index.dictionary)
