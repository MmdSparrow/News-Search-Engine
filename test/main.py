# import json
#
# stream_token = []
# # read json file
# f = open('../data/IR_data_news_12k.json')
# data = json.load(f)
#
# for i in range(0, 12202):
#     i_string = str(i)
#
#     # create index for title
#
#     # create index for content
#     stream_token += data[i_string]['content']
# f.close()
#
#
# def get_verb_with_mi():

#
# from test.A import A
# from test.B import B
#
# # s="hello     word  "
# # print(s.strip()+s)
#
#
# a = A()
# b = B()
#
#
# print(a.mylist)
#
# b.foo(a.myage, a.mylist)
#
# print(a.mylist)


# t_list=[("a",1),("b",2),("c",3)]
# test_tuple= ("test", 1)
# t_list[0]=("d",4)
# print(t_list)

# print(test_tuple.)

# dict = {
#     "1": 10000,
#     "2": 2,
#     "3": 3,
#     "70": 400,
#     "1000": 5,
#     "100": [12312312],
#     "13": [1231213312],
# }
#
# print(dict.keys())
#
# from parsivar.stemmer import FindStems
#
#
# def stem(word, word_pos=None):
#     return FindStems().convert_to_stem(word, word_pos)
#
# print(stem('می خواهد'))
# print(stem('میخواهد'))
# print(stem('میخواهد برود'))


A = ['1', 2, 'a']
B = ['1', 2]


def common_member(a, b):
    a_set = set(a)
    b_set = set(b)

    # check length
    if len(a_set.intersection(b_set)) > 0:
        return (a_set.intersection(b_set))
    else:
        return ("no common elements")


print(common_member(A, B))
