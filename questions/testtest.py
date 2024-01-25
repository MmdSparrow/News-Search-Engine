import re
from index.Tokenizer import Tokenizer
from preProcess.PreProcessor import PreProcessor

HALF_SPACE_CHARACTER = '\u200c'
another_half= '\u8204'
text = 'می‌‌شود'
text=text.replace("‌‌","‌")
print(text.__contains__('\u200c'))
print(text.__contains__('‌'))
result = re.split(r'\s+', text)
print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
print(result)
print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

regex_str = r'(?<!می)(?<!نمی)('+another_half+"|"+HALF_SPACE_CHARACTER+')+(?!ی)(?!ها)(?!تر)(?!گر)(?!ام)(?!اش)(?!های)(?!تری)(?!گری)(?!هایی)(?!ترین)(?!اعداد)'
print(regex_str)
final_result = []
for word in result:
    final_result.extend(re.split(regex_str, word))
print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
print(final_result)
print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")

text2 = 'می‌‌‌‌خواهم یکی را به قتل برسانم'
text2=text2.replace("‌‌","‌")
text2=text2.replace("‌‌","‌")
text2=text2.replace("‌‌","‌")
print("DDDDDDDDDDDDDDDDDddddd")
print(text2[2]==text2[3] and text2[2]=="‌")
print("Ddddddddddddddddddddd")
print(text2.__contains__('\u200c'))
print(text2.__contains__('‌'))
# text2.replace('', '‌')
result = re.split('\s+', text2)
final_result = []
# regex_str='‌+'
for word in result:
    final_result.extend(re.split(regex_str, word))

print("CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCcc")
print(final_result)

print(text[0] == text2[0])
print(text[1] == text2[1])
print(text[2] == text2[2])
print(text[3] == text2[3])
print(text[4] == text2[4])
print(text[5] == text2[5])
print(ord(text[3]))
print(text2[3])

# preprocessor = PreProcessor()
# query = preprocessor.query_preprocessor_handler(text)
# print(query)
