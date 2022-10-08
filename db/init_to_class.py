from txt_to_list import open_file
from word_class import KeyWord
from sqlite import set_value_in_db
'''
Methods for initialize list to class KeyWord
'''
def init_to_object_KeyWord(list, post):
    list_kw_objects = []
    for i in range(len(list)):
        keyword = KeyWord(post, id ,list[i] )
        list_kw_objects.append(keyword)
    return list_kw_objects



def init_to_class(filename,post):
    list_key_words = open_file(filename)   # list of objects KeyWord class
    set_value_in_db(list_key_words,post)






