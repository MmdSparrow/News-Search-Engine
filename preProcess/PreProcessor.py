from preProcess.FileReader import FileReader
from preProcess.Normalizer import Normalizer


class PreProcessor:
    def __init__(self):
        pass

    def document_preprocessor_handler(self):
        # read
        fileReader = FileReader()
        documents_length, documents_content, documents_title_url_dict = fileReader.read_file()
        print("reading file.....................................................................done")

        # normalize documents
        normalizer = Normalizer()
        normalizer.normalize_document(documents_content, documents_length)
        print("normalization.....................................................................done")

        return documents_length, documents_content, documents_title_url_dict

    def query_preprocessor_handler(self, query):
        normalizer = Normalizer()
        return normalizer.normalize_query(query)
