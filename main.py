import utils


text = utils.open_file('operations.json')
text1 = utils.get_last_operations(text)
for i in text1:
    print(i)

