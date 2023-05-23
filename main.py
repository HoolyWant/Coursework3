import utils


text = utils.open_file('operations.json')
#print(utils.last_operations_dates(text))

text1 = utils.get_last_operations(text)
# print(text[0])
print(text1)
for i in text1:
    print(i['date'])
#
# for i in text1:
#     print(i)