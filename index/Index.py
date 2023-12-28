class Index:
    def __init__(self):
        self.doc_frequency = 0
        self.postings_list = []

    def add_postings(self, postings):
        self.postings_list.append(postings)
        self.doc_frequency += 1

    def __str__(self):
        return f"#{self.doc_frequency} -> {self.postings_list}"

    def __repr__(self):
        return self.__str__()