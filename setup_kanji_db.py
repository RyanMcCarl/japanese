#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Set up dictionaries and database cursors of the most useful Japanese
kanji. Requires access to my kanji and word database.

.. moduleauthor:: Ryan McCarl <admin@wordbrewery.com>
"""
import pymongo

TESTKANJI = '騒'

db = pymongo.MongoClient().jp
assert db.kanji.count() > 2500
proj = {'_id': 0}
kanji_query = {"$and": [
        {"char": {"$exists": True}},
    {"$or": [
        {"joyo": True},
        {"kyoiku": True},
        {"rm2323": True},
        {"heisig": {"$exists": True}},
        {"henshall": {"$exists": True}},
        {"kklc": {"$exists": True}},
        {"rm_rank": {"$lt": 2400}},
        {"kanjidic": {"$lt": 2400}},
        {"mean": {"$lt": 2400}},
        {"rank": {"$lt": 2400}},
        {"freq": {"$lt": 2200}},
        {"variety": {"$lt": 2000}},
        {"wikipedia": {"$lt": 2000}},
        {"novels": {"$lt": 2000}},
        {"blogs": {"$lt": 2000}},
        {"top1000words": {"$exists": True}},
        {"top3000words": {"$exists": True}},
        {"top5000words": {"$exists": True}},
        {"top10000words": {"$exists": True}},
        {"top15000words": {"$exists": True}},
        {"top20000words": {"$exists": True}},
        {"top25000words": {"$exists": True}},
        {"twitter": {"$lt": 2000}},
        {"yatskov_novels": {"$lt": 2000}},
        {"aozora": {"$lt": 2000}}
            ]
        }
    ]
}

def make_kanji_dict():
    kcur = db.kanji.find(kanji_query, proj)
    kanji = {k['char']: k for k in kcur}
    return kanji

if __name__ == '__main__':
    make_kanji_dict()