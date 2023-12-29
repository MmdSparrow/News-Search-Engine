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

    def is_contains_doc_id(self, doc_id):
        for postings in self.postings_list:
            if postings.doc_id == doc_id:
                return True
        return False

    def get_postings_by_doc_id(self, doc_id):
        for postings in self.postings_list:
            if postings.doc_id == doc_id:
                return postings
        return None

