import heapq
from indexer.PositionalIndex import PositionalIndex
from scoring.ScoringVector import ScoringVector


class IRSystem:
    def __init__(self):
        self.K = 3

    def handler(self):
        positional_index, scoring_vector = self.__run_IR_system()
        while True:
            query = self.__interface()
            self.__search(query, positional_index, scoring_vector)

    def __search(self, query, positional_index, scoring_vector):
        doc_id_list = self.__find_k_most_similar_documents(query, positional_index.documents_title_url_dict.keys(), positional_index.document_length, positional_index.dictionary,
                                                           scoring_vector)
        for doc_id in range(len(doc_id_list)):
            print('doc_id: ' + str(doc_id))
            print('doc title: ' + str(doc_id_list[doc_id]))
            print('doc url: ' + str(doc_id_list[doc_id]))
            print('')

    def __run_IR_system(self):
        # phase 1: preprocessing and create positional index
        positional_index = PositionalIndex()
        positional_index.handler()

        # phase 2: scoring
        scoring_vector = ScoringVector()
        scoring_vector.create(positional_index.document_length, positional_index.dictionary)
        return positional_index, scoring_vector

    def __interface(self):
        print("please enter your query:")
        query = input()
        return query

    def __find_k_most_similar_documents(self, query, documents_id, documents_length, dictionary: dict, scoring_vector: ScoringVector):
        docId_similarity_list = []
        docId_similarity_size = 0
        for doc_id in documents_id:
            similarity = scoring_vector.similarity_query_and_doc(query, doc_id, documents_length, dictionary)
            if similarity != 0:
                # heapq sort tuple based on first element of tuple
                docId_similarity_list.append((similarity, doc_id))
                docId_similarity_size += 1
        self.__find_k_largest_element(docId_similarity_list, docId_similarity_size, self.K)
        return docId_similarity_list

    def __find_k_largest_element(self, array: list, array_size: int, k: int) -> list[str]:
        result = []
        pq = []
        heapq.heapify(pq)

        for i in range(array_size):

            heapq.heappush(pq, array[i])

            if (len(pq) > k):
                heapq.heappop(pq)

        while (len(pq) != 0):
            result.append(heapq.heappop(pq)[1])

        return result
