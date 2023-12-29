import heapq
from scoring.ScoringVector import ScoringVector
from preProcess.PreProcessor import PreProcessor
from index.CustomStemmer import CustomStemmer
from index.PriorityQueueWithFixedLength import PriorityQueueWithFixedLength


class ChampionsLists:
    def __init__(self):
        self.K = 5
        # [collection term frequency, document frequency (df_t), list of doc id]
        # [collection term frequency, document frequency (df_t), {doc_id: [document term frequency, tf-idf]}]
        self.champions_dict = {}

    def create(self, dictionary: dict):
        termp_champion_dict = self.__find_k_most_similar_documents_for_all_terms(dictionary)
        for word in termp_champion_dict:
            self.champions_dict[word] = [0, 0, {}]
            self.champions_dict[word][0] = dictionary[word][0]
            self.champions_dict[word][1] = dictionary[word][1]
            for doc_id in termp_champion_dict[word]:
                self.champions_dict[word][2][doc_id] = [0, 0]
                self.champions_dict[word][2][doc_id][0] = dictionary[word][2][doc_id][0]
                self.champions_dict[word][2][doc_id][1] = dictionary[word][2][doc_id][1]

    def __find_k_most_similar_documents_for_all_terms(self, dictionary):
        termp_champion_dict = {}
        for term in dictionary:
            max_list = []
            max_list_size = 0
            for doc_id in dictionary[term][2]:
                max_list.append((dictionary[term][2][doc_id][1], doc_id))
                max_list_size += 1
            termp_champion_dict[term] = self.__find_k_largest_element(max_list, max_list_size, self.K)
        return termp_champion_dict

    def search_query_in_champions_list(self, query: str, answer_dict, document_length, scoring_vector, main_dict):
        # normalize query
        preprocessor = PreProcessor()
        query = preprocessor.query_preprocessor_handler(query)

        # find k most similar in champion dict
        doc_id_list = self.__find_k_most_similar_documents(query, answer_dict.keys(), document_length, self.champions_dict, scoring_vector, main_dict)
        return doc_id_list

    def __find_k_most_similar_documents(self, query: str, documents_id: list, documents_length: int, dictionary: dict, scoring_vector: ScoringVector, main_dict=None):
        docId_similarity_list = []
        docId_similarity_size = 0
        for doc_id in documents_id:
            similarity = scoring_vector.similarity_query_and_doc(query, doc_id, documents_length, dictionary, True, main_dict)
            if similarity != 0:
                # heapq sort tuple based on first element of tuple
                docId_similarity_list.append((similarity, doc_id))
                docId_similarity_size += 1
        return self.__find_k_largest_element(docId_similarity_list, docId_similarity_size, self.K)

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
