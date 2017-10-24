#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# TODO: review, test, and refactor

"""
def main_kanji(kanji={}, perform_kanji_operations=None):
    from wbutilities import read_dict, write_files, update_mongo
    from wbkanji import add_synonyms, add_antonyms
    from os.path import expanduser
    kanji = {}

    assert (perform_kanji_operations == True)

    if get_kanji_from_dict_file:
        try:
            kanji = read_dict(dict_infile="~/japanese/kanji.dict", original_dict=kanji=)
            assert type(kanji) is DictType, "'kanji' is not a dictionary."
            assert len(kanji) > 2000, "'kanji' has a length of < 2000"
        except:
            e = "There was a problem with 'get_kanji_from_dict_file'"
            print(e)

    if get_kanji_synonyms_from_csv_file:
        # try:
        kanji = add_synonyms(csv_infile="~/japanese/kanji_synonyms.csv", original_dict=kanji=)
        assert type(kanji) is DictType, "'kanji' is not a dictionary."
        assert len(kanji) > 2000, "'kanji' has a length of < 2000"
        print(kanji)
        print(type(kanji))
        # except:
        # e = "There was a problem with 'get_kanji_synonyms_from_csv_file'"
        # print(e)

    if get_kanji_antonyms_from_csv_file:
        try:
            kanji = add_antonyms(csv_infile="~/japanese/kanji_antonyms.csv", original_dict=kanji=)
            assert type(kanji) is DictType, "'kanji' is not a dictionary."
            assert len(kanji) > 2000, "'kanji' has a length of < 2000"
            print(kanji)
            print(type(kanji))
        except:
            e = "There was a problem with 'get_kanji_antonyms_from_csv_file'"
            print(e)

    if write_kanji:
        try:
            kanji = write_files(entry_type="kanji", dict_data=kanji=)
            assert isinstance(kanji, dict), "'kanji' is not a dictionary."
            assert len(kanji) > 2000, "'kanji' has a length of < 2000"

        except:
            e = "There was a problem with 'write_files (kanji)'"
            print(e)

    if update_mongo_kanji:
        try:
            print(type(kanji))
            errors = update_mongo(dict_data=kanji, criteria='"char": key', db_name="jp", coll_name="kanji",
                                  errors=)
            assert isinstance(kanji, dict), "'kanji' is not a dictionary."
            assert len(kanji) > 2000, "'kanji' has a length of < 2000"
        except:
            e = "There was a problem with 'update_mongo_kanji'"
            print(e)

    print('Words: ', len(words))

    return kanji

"""

if __name__ == '__main__':
    pass
