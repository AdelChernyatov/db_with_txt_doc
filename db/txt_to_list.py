

def open_file(filename):
    file = open(filename, 'r', encoding = 'utf-8')
    list_of_words = []  # list for additions data from filename
    for item in file:
        if file == 'Бухгалетр.txt':
            list_of_words.append(item[2:])  #  input data features in 'accountant.txt'
        elif file  == 'gendir.txt':
            if item.isalpha():          #  input data features in 'gendir.txt'
                list_of_words.append(item)
        else:
            list_of_words.append(item)
        low_list_words = [i.lower() for i in list_of_words ] # list in low register
    return low_list_words

