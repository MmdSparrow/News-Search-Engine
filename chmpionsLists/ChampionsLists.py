import heapq
from scoring.ScoringVector import ScoringVector


class ChampionsLists:
    def __init__(self):
        self.K = 3
        self.champions_lists = {}

    def create_champions_lists_for_all_word(self, documents_id: list, documents_length: int, dictionary: dict, scoring_vector: ScoringVector):
        for word in dictionary.keys():
            self.champions_lists[word] = self.__find_k_most_similar_documents(word, documents_id, documents_length, dictionary, scoring_vector)

    def search_query_in_champions_list(self, query: str):
        # todo: normalize query
        # todo: stem query
        intersect_list = self.champions_lists[kalamat_query[0]]
        if len(intersect_list) == 0:
            return []
        for i in range(1, size_kalamat_query):
            intersect_list = self.__common_member(self.champions_lists[kalamat_query[i]], intersect_list)
            if len(intersect_list) == 0:
                return []
        return intersect_list

    def __common_member(self, first_list, second_list):
        first_set = set(first_list)
        second_set = set(second_list)

        if len(first_set.intersection(second_set)) > 0:
            return first_set.intersection(second_set)
        else:
            return []

    def __find_k_most_similar_documents(self, query: str, documents_id: list, documents_length: int, dictionary: dict, scoring_vector: ScoringVector):
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
            if len(pq) > k:
                heapq.heappop(pq)

        while len(pq) != 0:
            result.append(heapq.heappop(pq)[1])

        return result
