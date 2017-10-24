# !/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: review, test, and refactor

from wbutils.helpers import database

def main_words():
    """Collect data about words. Set configuration options in wbconfig.py to determine operations.

    Returns:
        TYPE: None
    """
    from os.path import expanduser
    # from wbutilities import read_dict, write_files, update_mongo
    from os.path import expanduser

    #words = {}

    """

    if get_words_from_json_file:
        from wbwords import add_words_from_json_file
        words = add_words_from_json_file(json_infile="~/japanese/jp_words.json", dict_data=words)

    if get_words_from_dict_file:
        from wbwords import add_words_from_dict_file
        words = add_words_from_dict_file(dict_infile="~/japanese/jp_words.dict", dict_data=words)

    if get_words_from_xml_file:
        from wbwords import add_words_from_xml_file
        words = add_words_from_xml_file(xml_infile="~/japanese/jdict.xml", dict_data=words)

    if get_words_from_jdict_file:
        from jdict import add_words_from_jdict_file
        words = add_words_from_jdict_file(words=words)

    if get_words_from_csv_file:
        from wbwords import add_words_from_csv_file
        words = add_words_from_csv_file(csv_infile='~/japanese/kwat.csv', dict_data=words)

    if write_words:
        words = write_files(entry_type="words", dict_data=words)

    if update_mongo_words:
        errors = update_mongo(dict_data=words, criteria='"word": key', db_name="jp", coll_name="words")

    print('Words: ', len(words))
    
    """

    # return words

def make_char_dict(db_name="jp"):
    localdb = database.connect_mongo()
    remotedb = database.connect_mlab()

    # Prepare word dict
    words = localdb.words.find()

    # Prepare char dict for Japanese or Chinese (if needed)
    if db_name not in ["jp", "ch"]:
        print("Not retrieving characters because you are not looking up the Japanese or Chinese database")
        return {}
    elif db_name is "jp":
        coll_name = "kanji"
    elif db_name is "ch":
        coll_name = "hanzi"

    return db_name.coll_name.find({'char': {'exists': True}}, {'_id': 0})

def make_word_dict(db_name="jp", coll_name="words"):
    db = database.connect_mongo()

    words = localdb.coll_name.find()

    # try:
    #    remotedb = database.connect_mlab()
    # except:
    #    print("Cannot connect to mlab for the database {}".format(db_name))

    else:
        coll_name = input("What collection should I add to the dict?")

    words = {w['word']: w.items() for w in ws}

    # Prepare kanji dict


if __name__ == '__main__':
    make_word_dict()
