import json

HALF_SPACE_CHAR = chr(0x200c)


def doc_tokenize(doc_id: str, doc_string: str) -> list[tuple[str, int, str]]:
    doc_stream_token = []
    word = ''
    position = 1
    for char in doc_string.strip():
        # be nazaram in " or char == half_space_char " nabashe behtare
        if (char == ' ' or char == '\t' or char == '\n') and word != 'می':
            if word.strip() != '':
                doc_stream_token.append((word, position, doc_id))
                word = ''
                position += 1
        else:
            word += char

    if word.strip() != '':
        doc_stream_token.append((word, position, doc_id))

    return doc_stream_token



def tokenize() -> list[tuple[str, int, str]]:
    stream_token = []
    # read json file
    f = open('../data/IR_data_news_12k.json')
    data = json.load(f)

    for i in range(0, 12202):
        i_string = str(i)

        # create index for title

        # create index for content
        stream_token += doc_tokenize(i_string, data[i_string]['content'])
    f.close()

    return stream_token
