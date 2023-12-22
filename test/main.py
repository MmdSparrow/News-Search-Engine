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

import parsivar

from test.A import A
from test.B import B

# s="hello     word  "
# print(s.strip()+s)


a = A()
b = B()


print(a.mylist)

b.foo(a.myage, a.mylist)

print(a.mylist)