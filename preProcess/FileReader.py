import json


class FileReader:
    DEFAULT_PATH = '../data/IR_data_news_12k.json'

    def __init__(self):
        pass

    def read_file(self, documents_content, path: str = DEFAULT_PATH):
        f = open(path)
        data = json.load(f)
        documents_len = len(data)
        # for test uncomment following line
        documents_len = 2

        for i in range(0, documents_len):
            i_string = str(i)
            # read title
            # todo:
            # read content
            documents_content.append(data[i_string]['content'].strip())

        f.close()

        return documents_len
