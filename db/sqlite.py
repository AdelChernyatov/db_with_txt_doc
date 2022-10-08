import sqlite3
from txt_to_list import open_file
from word_class import KeyWord


conn = sqlite3.connect('key_word.db')

c = conn.cursor()

#c.execute(""" CREATE TABLE keywords (
 #   post text,
 #   id text,
 #   word text
 #   )""")
#c.execute("INSERT INTO key_words VALUES ('buchgalter',1 ,'Excel')")
#c.execute("INSERT INTO key_words VALUES ('buchgalter',1 ,'high education')")


#c.execute("SELECT * FROM key_words WHERE id = 1 ")
#print(c.fetchall())

def init_to_class(filename, post):
    list_key_words = open_file(filename)   # list of objects KeyWord class
    set_value_in_db(list_key_words, post)


def set_value_in_db(list, post):
    for i in range(len(list)):
       keyword = KeyWord(id, post, list[i])
       c.execute("INSERT INTO keywords VALUES (?, ?, ?)", (keyword.post, str(keyword.id), keyword.text))
       conn.commit()
    c.execute("SELECT * FROM keywords WHERE post = 'accountant' ")
    print(c.fetchall())
    conn.commit()




