from indexer.LinguisticModule import LinguisticModule
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
        linguistic_module = LinguisticModule()
        linguistic_module.delete_50_most_repeated_words(self.dictionary)

        tokenizer = Tokenizer()
        tokenizer.tokenize(document_content, document_length, self.dictionary, linguistic_module.most_repeated_word,
                           linguistic_module.stemmer)

        print(self.dictionary)