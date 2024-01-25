import heapq
import pickle
from index.PositionalIndex import PositionalIndex
from preProcess.PreProcessor import PreProcessor
from scoring.ScoringVector import ScoringVector
from chmpionsIndex.ChampionsLists import ChampionsLists


class IRSystem:
    def __init__(self):
        self.K = 3
        self.DATASTORE_PATH = 'datastore/'

    def handler(self):
        # starting......
        print("starting.....................................................................")
        # for first time
        positional_index, scoring_vector, champions_list = self.__run_IR_system_by_creating()
        # OW
        # positional_index, scoring_vector, champions_list = self.__run_IR_system_by_loading()
        while True:
            query = self.__interface()
            self.__search(query, positional_index, scoring_vector, champions_list)

    def __search(self, query, positional_index, scoring_vector, champions_list):
        # self, query: str, answer_dict, document_length, scoring_vector
        doc_id_list = champions_list.search_query_in_champions_list(query, positional_index.documents_title_url_dict, positional_index.document_length, scoring_vector,
                                                                    self.K, positional_index.dictionary)
        reminded = self.K - len(doc_id_list)
        if reminded != 0:
            doc_id_list = self.__search_query_in_main_index(query, positional_index.documents_title_url_dict, positional_index.document_length, scoring_vector, self.K, positional_index.dictionary)
        if (len(doc_id_list) == 0):
            print("No result!")
        else:
            for i in range(min(len(doc_id_list), self.K)):
                print('doc_id: ' + str(doc_id_list[len(doc_id_list)-1-i]))
                print('doc title: ' + positional_index.documents_title_url_dict[str(doc_id_list[len(doc_id_list)-1-i])][0])
                print('doc url: ' + positional_index.documents_title_url_dict[str(doc_id_list[len(doc_id_list)-1-i])][1])
                print('')

    def __run_IR_system_by_creating(self):
        # phase 1: preprocessing and create positional index
        positional_index = PositionalIndex()
        positional_index.create()
        print("creating index.....................................................................done")

        # phase 2: scoring
        scoring_vector = ScoringVector()
        scoring_vector.create(positional_index.document_length, positional_index.dictionary)
        print("creating vector space.....................................................................done")

        # phase 3: champion list
        champions_lists = ChampionsLists()
        champions_lists.create(positional_index.dictionary)
        print("creating champion list.....................................................................done")

        # store these three objects
        file_positional_index = open(self.DATASTORE_PATH + 'positional_index', 'wb')
        pickle.dump(positional_index, file_positional_index)
        file_positional_index.close()
        print("storing index.....................................................................done")

        file_scoring_vector = open(self.DATASTORE_PATH + 'scoring_vector', 'wb')
        pickle.dump(scoring_vector, file_scoring_vector)
        file_scoring_vector.close()
        print("storing vector space.....................................................................done")

        file_champions_lists = open(self.DATASTORE_PATH + 'champion_list', 'wb')
        pickle.dump(champions_lists, file_champions_lists)
        file_champions_lists.close()
        print("storing champion list.....................................................................done")

        return positional_index, scoring_vector, champions_lists

    def __run_IR_system_by_loading(self):
        # phase 1: preprocessing and create positional index
        file_positional_index = open(self.DATASTORE_PATH + 'positional_index', 'rb')
        positional_index = pickle.load(file_positional_index)
        file_positional_index.close()

        # phase 2: scoring
        file_scoring_vector = open(self.DATASTORE_PATH + 'scoring_vector', 'rb')
        scoring_vector = pickle.load(file_scoring_vector)
        file_scoring_vector.close()

        # phase 3: champion list
        champions_lists_vector = open(self.DATASTORE_PATH + 'champion_list', 'rb')
        champions_lists = pickle.load(champions_lists_vector)
        champions_lists_vector.close()

        return positional_index, scoring_vector, champions_lists

    def __interface(self):
        print("please enter your query:")
        query = input()
        return query

    def __search_query_in_main_index(self, query: str, answer_dict, document_length, scoring_vector, K, main_dict):
        # normalize query
        preprocessor = PreProcessor()
        query = preprocessor.query_preprocessor_handler(query)

        # find k most similar in champion dict
        doc_id_list = self.__find_k_most_similar_documents(query, answer_dict.keys(), document_length,
                                                           main_dict, scoring_vector, K)
        return doc_id_list

    def __find_k_most_similar_documents(self, query: str, documents_id: list, documents_length: int, dictionary: dict,
                                        scoring_vector: ScoringVector, K, main_dict=None):
        docId_similarity_list = []
        docId_similarity_size = 0
        for doc_id in documents_id:
            similarity = scoring_vector.similarity_query_and_doc(query, doc_id, documents_length, dictionary, False,
                                                                 main_dict)
            if similarity != 0:
                # heapq sort tuple based on first element of tuple
                docId_similarity_list.append((similarity, doc_id))
                docId_similarity_size += 1
        return self.__find_k_largest_element(docId_similarity_list, docId_similarity_size, K)

    def __find_k_largest_element(self, array: list, array_size: int, k: int) -> list[str]:
        result = []
        pq = []
        heapq.heapify(pq)

        for i in range(array_size):
            heapq.heappush(pq, array[i])
            if len(pq) > k:
                heapq.heappop(pq)

        while len(pq) != 0:
            result.append(heapq.heappop(pq)[1])

        return result
