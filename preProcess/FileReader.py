import json


class FileReader:
    DEFAULT_PATH = './data/IR_data_news_12k.json'

    def __init__(self):
        pass

    def read_file(self, path: str = DEFAULT_PATH):
        documents_content = []

        f = open(path)
        data = json.load(f)
        documents_len = len(data)
        # for test uncomment following line
        # documents_len = 10
        documents_title_url_dict = {}

        for i in range(0, documents_len):
            i_string = str(i)
            # read title
            documents_title_url_dict[i_string] = (data[i_string]['title'], data[i_string]['url'])

            # read content
            documents_content.append(data[i_string]['content'].strip())

            # test
            # print(data[i_string]['content'].strip())

        f.close()

        return documents_len, documents_content, documents_title_url_dict
