from json import load


def open_file(file):
    with open(file, encoding='utf-8') as text:
        dict_ = load(text)
        return dict_




