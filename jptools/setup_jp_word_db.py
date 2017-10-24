#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Set up dictionaries and database cursors of the most useful Japanese
words. Requires access to my kanji and word database.

.. moduleauthor:: Ryan McCarl <admin@wordbrewery.com>

"""

import pymongo

TESTWORD = '自然'
proj = {'_id': 0}
word_query = {'$and': [
        {'word': {'$exists': True}},
        {'jdict': {'$exists': True}},
        {'$or':
            [
                {'edict_common': True},
                {'rmjf': {'$lt': 30000}},
                {'jdict': {'$lt': 30000}},
                {'edict': {'$lt': 30000}},
                {'mainichi': {'$lt': 25000}},
                {'wikipedia': {'$lt': 25000}},
                {'blogs2008': {'$lt': 20000}},
                {'leeds': {'$lt': 15000}},
                {'kwat': {'$lt': 15000}},
                {'wb': {'$lt': 15000}},
                {'kyoiku_words': {'$exists': True}}
            ]
        }
    ]
}

def get_japanese_db():
    db = pymongo.MongoClient().jp
    assert db.words.count() > 50000
    return db

def get_words_collection():
    db = get_japanese_db()
    return db.words

def get_all_words():
    db = get_japanese_db()
    return db.words.find(word_query, proj)

def make_word_dict():
    db = get_japanese_db()
    wcur = db.words.find(word_query, proj)
    words = {w['word']: w for w in wcur}
    wcur.close()

    return words

if __name__ == '__main__':
    japanese_db = get_japanese_db()
    all_words = get_all_words()
    word_coll = get_words_collection()
    word_dict = make_word_dict()

