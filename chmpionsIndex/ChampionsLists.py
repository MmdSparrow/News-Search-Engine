import heapq
from scoring.ScoringVector import ScoringVector
from preProcess.PreProcessor import PreProcessor
from index.CustomStemmer import CustomStemmer


class ChampionsLists:
    def __init__(self):
        self.K = 5
        # [collection term frequency, document frequency (df_t), list of doc id]
        # [collection term frequency, document frequency (df_t), {doc_id: [document term frequency, tf-idf]}]
        self.champions_dict = {}

    def create(self, documents_id: list, documents_length: int, dictionary: dict, scoring_vector: ScoringVector):
        champions_lists = {}
        for word in dictionary.keys():
            champions_lists[word] = self.__find_k_most_similar_documents(word, documents_id, documents_length, dictionary, scoring_vector)
        for word in champions_lists.keys():
            self.champions_dict[word] = []
            self.champions_dict[word][0] = dictionary[word][0]
            self.champions_dict[word][1] = dictionary[word][1]
            self.champions_dict[word][2] = {}
            for doc_id in champions_lists[word]:
                self.champions_dict[word][2][doc_id] = []
                self.champions_dict[word][2][doc_id][0] = dictionary[word][2][doc_id][0]
                self.champions_dict[word][2][doc_id][1] = dictionary[word][2][doc_id][1]

    def search_query_in_champions_list(self, query: str, answer_dict, document_length, scoring_vector):
        # normalize query
        preprocessor = PreProcessor()
        query = preprocessor.query_preprocessor_handler(query)

        # find k most similar in champion dict
        doc_id_list = self.__find_k_most_similar_documents(query, answer_dict.keys(), document_length, self.champions_dict, scoring_vector)
        return doc_id_list

    def __find_k_most_similar_documents(self, query: str, documents_id: list, documents_length: int, dictionary: dict, scoring_vector: ScoringVector):
        docId_similarity_list = []
        docId_similarity_size = 0
        for doc_id in documents_id:
            similarity = scoring_vector.similarity_query_and_doc(query, doc_id, documents_length, dictionary)
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
