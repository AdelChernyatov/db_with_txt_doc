import sqlite3
from txt_to_list import open_file
from word_class import KeyWord


conn = sqlite3.connect('KeyWord.db')

c = conn.cursor()
'''
Create db Table
'''
#c.execute(""" CREATE TABLE Keywords (
 #   post text,
  #  id integer,
  #  word text
  #  )""")

def init_to_class(filename, post):
    list_key_words = open_file(filename)   # list of objects KeyWord class
    set_value_in_db(list_key_words, post)


def set_value_in_db(list, post):
   for id in range(len(list)):
       keyword = KeyWord(id, post, list[id])    # make object KeyWord from object list
       c.execute("INSERT INTO Keywords VALUES (?, ?, ?)", (keyword.post, keyword.id, keyword.text))
       conn.commit()   # input data from db





