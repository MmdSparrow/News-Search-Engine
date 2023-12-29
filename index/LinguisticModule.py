from index.PriorityQueueWithFixedLength import PriorityQueueWithFixedLength
from index.CustomStemmer import CustomStemmer


class LinguisticModule:
    def __init__(self):
        self.most_repeated_word = PriorityQueueWithFixedLength()
        self.stemmer = CustomStemmer()

    # def delete_50_most_repeated_words(self, dictionary: dict):
    #     for i in range(min(self.most_repeated_word.capacity, len(dictionary))):
    #         dictionary.pop(self.most_repeated_word.queue[i][0])

    def delete_50_most_repeated_words_stem_remains_from_tokens(self, stream_token):
        new_tokens_list = []
        for token in stream_token:
            if not self.most_repeated_word.is_contain(token[0]):
                new_tokens_list.append((self.stemmer.stem(token[0]), token[1], token[2]))
        self.__report(len(stream_token), len(new_tokens_list))
        return new_tokens_list

    def __report(self, stream_token_length, new_stream_token_length):
        print("##########################################################################################")
        total_frequency = 0
        for i in range(len(self.most_repeated_word.queue)):
            word, freq = self.most_repeated_word.queue[i]
            print(f'{i + 1}- (Word, Frequency):({word}, {freq})')
            total_frequency += freq
        print(f'Total Frequency: {total_frequency}')
        print(f'Stream Token Length: {stream_token_length}')
        print(f'New Stream Token Length: {new_stream_token_length}')
        print("##########################################################################################")
