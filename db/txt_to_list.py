
def open_file(filename):
    file = open(filename, 'r', encoding = 'utf-8')
    list_of_words = []  # list for additions data from filename
    if filename == 'accountant.txt':
        for item in file:
            list_of_words.append(item[2:])  # input data features in 'accountant.txt'
    else:
        for item in file:
            list_of_words.append(item)
    low_list_words = [i.lower() for i in list_of_words ] # list in low register
    return low_list_words
