class Postings:
    def __init__(self, doc_id):
        self.doc_id = doc_id
        self.term_frequency = 0
        self.tf_idf = -1
        self.positions = []

    def add_posting(self, position):
        self.positions.append(position)
        self.term_frequency += 1

    def __str__(self):
        return f"{self.doc_id} : #{self.term_frequency} -> {self.positions}"

    def __repr__(self):
        return self.__str__()
