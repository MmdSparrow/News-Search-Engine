import heapq
from scoring.ScoringVector import ScoringVector
from preProcess.PreProcessor import PreProcessor
from index.Index import Index


class ChampionsLists:
    def __init__(self):
        self.K = 5
        self.champions_dict = {}

    def create(self, doc_id_list: list, documents_length: int, dictionary: dict, scoring_vector: ScoringVector):
        champions_lists = {}

        for word in dictionary:
            champions_lists[word] = self.__find_k_most_similar_documents(word, doc_id_list, documents_length, dictionary, scoring_vector, main_dict=dictionary)
        for word in champions_lists:
            self.champions_dict[word] = Index()
            self.champions_dict[word].doc_frequency = dictionary[word].doc_frequency
            for doc_id in champions_lists[word]:
                self.champions_dict[word].postings_list.appened(dictionary[word].get_postings_by_doc_id(doc_id))

    def search_query_in_champions_list(self, query: str, doc_id_list, document_length, scoring_vector, main_dict):
        # normalize query
        preprocessor = PreProcessor()
        query = preprocessor.query_preprocessor_handler(query)

        # find k most similar in champion dict
        return self.__find_k_most_similar_documents(query, doc_id_list, document_length, self.champions_dict, scoring_vector, main_dict)

    def __find_k_most_similar_documents(self, query, doc_id_list: list, document_length: int, dictionary: dict, scoring_vector: ScoringVector, main_dict=None) -> list[
        str]:  # dict[word] = doc id
        docId_similarity_tuples = []
        for doc_id in doc_id_list:
            similarity = scoring_vector.similarity_query_and_doc(query, doc_id, document_length, dictionary, True, main_dict)
            if similarity != 0:
                # heapq sort tuple based on first element of tuple
                docId_similarity_tuples.append((similarity, doc_id))
        return self.__find_k_largest_element(docId_similarity_tuples, self.K)

    def __find_k_largest_element(self, array: list, k: int) -> list[str]:
        result = []
        pq = []
        heapq.heapify(pq)

        for i in range(len(array)):
            heapq.heappush(pq, array[i])
            if len(pq) > k:
                heapq.heappop(pq)

        while len(pq) != 0:
            result.append(heapq.heappop(pq)[1])

        return result
