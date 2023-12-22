from FileReader import FileReader
from DocumentNormalization import DocumentNormalization


class PreProcessor:
    def __init__(self):
        pass

    def handler(self):
        documents_content = []

        # read
        fileReader = FileReader()
        documents_length = fileReader.read_file(documents_content)

        # normalize documents
        documentNormalization = DocumentNormalization()
        documentNormalization.normalize(documents_content, documents_length)

        return documents_length, documents_content
