import math
from preProcess.PreProcessor import PreProcessor
from index.CustomStemmer import CustomStemmer


class ScoringVector:
    def __init__(self):
        pass

    def create(self, documents_length: int, dictionary: dict):
        # doc id, sqrt(w1^2+w2^2+....)
        doc_cosine_normalization_denominator = {}
        for word in dictionary.keys():
            for doc_id in dictionary[word][2]:
                self.__document_tf_idf_calculator(word, doc_id, documents_length, dictionary)
                if doc_id in doc_cosine_normalization_denominator:
                    doc_cosine_normalization_denominator[doc_id] += dictionary[word][2][doc_id][1]
                else:
                    doc_cosine_normalization_denominator[doc_id] = dictionary[word][2][doc_id][1]
                    # now we normalize calculated weight
        for word in dictionary.keys():
            for doc_id in dictionary[word][2]:
                dictionary[word][2][doc_id][1] = dictionary[word][2][doc_id][1] / doc_cosine_normalization_denominator[doc_id]

    def __document_tf_idf_calculator(self, term: str, doc_id: str, documents_length: int, dictionary: dict):
        dictionary[term][2][doc_id][1] = (1 + math.log(dictionary[term][2][doc_id][0], 10)) * math.log(documents_length / dictionary[term][1], 10)

    def similarity_query_and_doc(self, query, doc_id: str, documents_length: int, dictionary: dict, is_champion_list=False, main_dict=None):
        similarity = 0
        query_tf_idf = self.__query_tf_idf_calculator(query, documents_length, dictionary, is_champion_list, main_dict)
        for word in query_tf_idf.keys():
            if word in dictionary and doc_id in dictionary[word][2]:
                similarity += query_tf_idf[word] * dictionary[word][2][doc_id][1]
        return similarity

    def __query_tf_idf_calculator(self, query: str, documents_length: int, dictionary: dict, is_champion_list=False, main_dict=None) -> dict:
        # at first we normalize query
        if not is_champion_list:
            preprocessor = PreProcessor()
            query = preprocessor.query_preprocessor_handler(query)
        query_word_frequency_dict = self.__word_frequency_in_query_calculator(query)
        query_tf_idf = {}
        query_cosine_normalization_denominator = 0
        # chon bayad az ruye main_dict tf_idf champion list ha hesab beshe ama tuye champion_dict por beshe bayad main_dict ro ham dashte bashim
        if is_champion_list and main_dict is not None:
            for word in query_word_frequency_dict.keys():
                # we have to check it is  exist in dictionary
                if word in main_dict:
                    query_tf_idf[word] = (1 + math.log(query_word_frequency_dict[word], 10)) * math.log((documents_length + 1) / main_dict[word][1], 10)
                    query_cosine_normalization_denominator += query_tf_idf[word]
        else:
            for word in query_word_frequency_dict.keys():
                # we have to check it is  exist in dictionary
                if word in dictionary:
                    query_tf_idf[word] = (1 + math.log(query_word_frequency_dict[word], 10)) * math.log((documents_length + 1) / dictionary[word][1], 10)
                    query_cosine_normalization_denominator += query_tf_idf[word]
        # cosine normalize
        for word in query_tf_idf.keys():
            query_tf_idf[word] = query_tf_idf[word] / query_cosine_normalization_denominator
        return query_tf_idf

    def __word_frequency_in_query_calculator(self, query: str):
        customStemmer = CustomStemmer()
        word_frequency = {}
        word = ''
        for char in query.strip():
            if char == ' ' or char == '\t' or char == '\n':
                word = word.strip()
                word = customStemmer.stem(word)
                if word != '':
                    # if word already is in word_frequency
                    if word in word_frequency:
                        word_frequency[word] += 1
                    else:
                        word_frequency[word] = 1
                    word = ''
            else:
                word += char

        word = word.strip()
        word = customStemmer.stem(word)
        if word != '':
            if word in word_frequency:
                word_frequency[word] += 1
            else:
                word_frequency[word] = 1

        return word_frequency
