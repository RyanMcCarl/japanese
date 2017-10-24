#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""WordBrewery utilities

.. moduleauthor:: Ryan McCarl <admin@wordbrewery.com>

"""

import pymongo
db = pymongo.MongoClient().jp
assert db.words.count() > 100000
assert db.kanji.count() > 100000

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

words = db.words.find(query, proj)
assert words.count() > 30000

worddict = {w['word']: w.items() for w in words}

next(words)
{'word': '鎮座', 'pos': "['n', 'vs']", 'meaning': ['enshrinement'], 'reading': 'ちんざ', 'edict': 15300, 'blogs_2008': 15322, 'kwat': 13165, 'mainichi': 36025, 'wikipedia': 8867, 'rmjf': 14675, 'wb': 24198, 'jdict': 20764, 'kic': 6698, 'chars': ['座', '鎮']}
next(words)
{'word': '揺', 'pos': 'n', 'meaning': ['flickering', 'jolting', 'tremor', 'vibration'], 'reading': 'ゆり', 'edict': 33633, 'blogs_2008': 33673, 'kwat': 14395, 'mainichi': 62404, 'wikipedia': 38573, 'rmjf': 33832, 'wb': 39094, 'jdict': 22994, 'chars': ['揺']}
next(words)
{'word': '弁論', 'pos': "['n', 'vs', 'adj-no']", 'meaning': ['argument', 'debate', 'discussion'], 'reading': 'べんろん', 'edict': 25793, 'blogs_2008': 25824, 'kwat': 19546, 'mainichi': 11661, 'wikipedia': 18975, 'leeds': 10831, 'rmjf': 19281, 'wb': 16814, 'jdict': 30835, 'chars': ['弁', '論'], 'edict_common': True, 'kyoiku_words': ['弁論']}
next(words)
{'word': '収集', 'pos': "['n', 'vs']", 'meaning': ['accumulation', 'collection', 'gathering up'], 'reading': 'しゅうしゅう', 'edict': 2517, 'blogs_2008': 2522, 'kwat': 9282, 'mainichi': 3028, 'wikipedia': 3834, 'leeds': 2460, 'rmjf': 4049, 'wb': 3881, 'jdict': 14116, 'kic': 1163, 'chars': ['収', '集'], 'edict_common': True, 'kyoiku_words': ['収集']}
words = db.words.find(query, proj)
kyoiku_words = words.find({'kyoiku_words': {'exists': True}})
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Cursor' object has no attribute 'find'
kyoiku_words = db.words.find({'kyoiku_words': {'exists': True}}, {'_id': 0})
kyoiku_words.co
kyoiku_words.collation(   kyoiku_words.collection(  kyoiku_words.comment(     kyoiku_words.count(
kyoiku_words.count()
0
kyoiku_words = db.words.find({'kyoiku_words': {'$exists': True}}, {'_id': 0})
kyoiku_words.count()
17851
worddict = {w['word']: w.items() for w in kyoiku_words}
worddict.update({w['word']: w.items() for w in words})
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 1, in <dictcomp>
KeyError: 'word'
kyoiku_words.count()
17851
query = {'$and': [{'word': {'$exists': True}}, '$or': [{'edict_common': True}, {'rmjf': {'$lt': 30000}}, {'jdict': {'$lt': 30000}}]}
  File "<stdin>", line 1
    query = {'$and': [{'word': {'$exists': True}}, '$or': [{'edict_common': True}, {'rmjf': {'$lt': 30000}}, {'jdict': {'$lt': 30000}}]}
                                                        ^
SyntaxError: invalid syntax
query = {'$and': [{'word': {'$exists': True}}, '$or': [{'edict_common': True}, {'rmjf': {'$lt': 30000}}, {'jdict': {'$lt': 30000}}]}}
  File "<stdin>", line 1
    query = {'$and': [{'word': {'$exists': True}}, '$or': [{'edict_common': True}, {'rmjf': {'$lt': 30000}}, {'jdict': {'$lt': 30000}}]}}
                                                        ^
SyntaxError: invalid syntax
query = {'$and': [{'word': {'$exists': True}}, '$or': [{'edict_common': True}, {'rmjf': {'$lt': 30000}}, {'jdict': {'$lt': 30000}}]]}
  File "<stdin>", line 1
    query = {'$and': [{'word': {'$exists': True}}, '$or': [{'edict_common': True}, {'rmjf': {'$lt': 30000}}, {'jdict': {'$lt': 30000}}]]}
                                                        ^

len(worddict)
38080
db.kanji.find_one()
{'_id': ObjectId('59599c74bec0545e33723c73'), 'radicals': ['巾', '辶', '厂', '二', '｜'], 'rm_rank': 2404, 'yatskov_novels': 3413, 'onyomi': ['テイ'], 'freq': 1957, 'radical_list': '逓', 'hanja': '체', 'wikipedia': 2609, 'kunyomi': ['たがいに', 'かわ.る'], 'jlpt': 1, 'pinyin': 'di4', 'average': 2448, 'grade': 8, 'variants': ['遞'], 'kklc': 1555, 'novels': 3683, 'variety': 3183, 'mainichi': 2172, 'rm2323': True, 'components': ['巾', '辶', '厂', '二', '丨', '乕', '辶'], 'kanjidic': 1957, 'kic': 1980, 'twitter': 3215, 'rank': 2365, 'peers': ['逞', '逗', '遁', '遙', '遵', '遽', '挺', '蹄', '醍', '掟', '禎', '砥', '體', '鼎'], 'heisig': 2002, 'aozora': 3717, 'rtk_two_examples': 1843, 'stroke_count': 9, 'top15000words': ['逓信'], 'henshall': 1618, 'gsf': 1972, 'char': '逓', 'mean': 2455, 'count': 16, 'median': 2087, 'minimum': 1555, 'joyo': True}
kanjidict = db.kanji.find({'$or': [{'joyo': True}, {'kyoiku': True}, {'rm_rank': {'$lt': 2500}}]}}, {'_id': 0})
  File "<stdin>", line 1
    kanjidict = db.kanji.find({'$or': [{'joyo': True}, {'kyoiku': True}, {'rm_rank': {'$lt': 2500}}]}}, {'_id': 0})
                                                                                                     ^
SyntaxError: invalid syntax
kanjidict = db.kanji.find({'$or': [{'joyo': True}, {'kyoiku': True}, {'rm_rank': {'$lt': 2500}}]}, {'_id': 0})
kanjidict.count()
2259
kanjidict = db.kanji.find({'$or': [{'joyo': True}, {'kyoiku': True}, {'heisig': {'$exists': True}}, {'kklc': {'$exists': True}}, {'rm_rank': {'$lt': 2500}}]}, {'_id': 0})
kanjidict.count()
2276
kanjidict = db.kanji.find({'$or': [{'joyo': True}, {'kyoiku': True}, {'heisig': {'$exists': True}}, {'kklc': {'$exists': True}}, {'rm_rank': {'$lt': 2500}}, {'jlpt': {'$exists': True}}, {'kanjidict': {'$lt': 2500}}     ]}, {'_id': 0})
kanjidict.count()
2459
kanjidict = db.kanji.find({'$or': [{'joyo': True}, {'kyoiku': True}, {'heisig': {'$exists': True}}, {'kklc': {'$exists': True}}, {'rm_rank': {'$lt': 2500}}, {'jlpt': {'$exists': True}}, {'kanjidict': {'$lt': 2500}}, {'rm2323': True}}     ]}, {'_id': 0})
  File "<stdin>", line 1
    kanjidict = db.kanji.find({'$or': [{'joyo': True}, {'kyoiku': True}, {'heisig': {'$exists': True}}, {'kklc': {'$exists': True}}, {'rm_rank': {'$lt': 2500}}, {'jlpt': {'$exists': True}}, {'kanjidict': {'$lt': 2500}}, {'rm2323': True}}     ]}, {'_id': 0})
                                                                                                                                                                                                                                            ^
SyntaxError: invalid syntax
kanjidict = db.kanji.find({'$or': [{'joyo': True}, {'kyoiku': True}, {'heisig': {'$exists': True}}, {'kklc': {'$exists': True}}, {'rm_rank': {'$lt': 2500}}, {'jlpt': {'$exists': True}}, {'kanjidict': {'$lt': 2500}}, {'rm2323': True}     ]}, {'_id': 0})
kanjidict.count()
2459
>>>