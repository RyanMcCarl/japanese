
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
>>> kanjidictword_query = {'$and': [
...         {'word': {'$exists': True}},
...         {'jdict': {'$exists': True}},
...         {'$or':
KeyboardInterrupt
>>> kanjidict[’本']]
  File "<stdin>", line 1
    kanjidict[’本']]
               ^
SyntaxError: invalid character in identifier
>>> kanjidict[’本']
  File "<stdin>", line 1
    kanjidict[’本']
               ^
SyntaxError: invalid character in identifier
>>> kanjidict[u’本']
  File "<stdin>", line 1
    kanjidict[u’本']
                ^
SyntaxError: invalid character in identifier
>>> kanjidict['本']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python3.6/site-packages/pymongo/cursor.py", line 572, in __getitem__
    "instances" % index)
TypeError: index '本' cannot be applied to Cursor instances
>>> kanjidict['本']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python3.6/site-packages/pymongo/cursor.py", line 572, in __getitem__
    "instances" % index)
TypeError: index '本' cannot be applied to Cursor instances
>>> type(kanjidict)
<class 'pymongo.cursor.Cursor'>
>>> kanjidict.count()
2459
>>> kanji.count()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'kanji' is not defined
>>> kanji = {w['char']: w.items() for w in kanjidict}}
  File "<stdin>", line 1
    kanji = {w['char']: w.items() for w in kanjidict}}
                                                     ^
SyntaxError: invalid syntax
>>> kanji = {w['char']: w.items() for w in kanjidict}
>>> len(kanji)
2459
>>> kanji['本']
dict_items([('radicals', ['一', '木']), ('rm_rank', 4), ('yatskov_novels', 34), ('onyomi', ['ホン']), ('top3000words', ['本人', '東日本', '本当', '日本人', '日本語', '本の', '基本的', '本来', '本気', '本物', '絵本', '本番', '本格的', '一本', '基本的に', '本音', '日本一', '本店', '本館', '本部', '全日本', '本体', '本格', '本質', '西日本', '本社', '本編', '資本', '根本', '本能', '本線', '本塁打', '本書', '文庫本', '本会議', '本性']), ('freq', 10), ('radical_list', '本'), ('hanja', '본'), ('wikipedia', 7), ('kunyomi', ['もと']), ('jlpt', 4), ('pinyin', 'ben3'), ('average', 35), ('grade', 1), ('kyoiku', True), ('variants', ['夲']), ('kklc', 31), ('novels', 29), ('variety', 7), ('mainichi', 4), ('rm2323', True), ('components', ['一', '木', '体', '笨', '躰', '鉢']), ('kanjidic', 10), ('kic', 2), ('twitter', 16), ('rank', 7), ('peers', ['果', '業', '条', '末', '東', '案', '木', '村', '校', '格', '森', '楽', '様', '機', '世', '由', '申', '内', '表', '出', '史', '向', '下', '元', '品', '反']), ('lookalikes', ['休', '体']), ('heisig', 224), ('aozora', 27), ('blogs', 109), ('rtk_two_examples', 165), ('stroke_count', 5), ('top15000words', ['新日本製鉄', '本郷', '本間', '絹本', '本欄', '本田', '東日本', '本案', '本日', '本文', '本番', '基本的に', '日本一', '本屋', '本棚', '脚本', '本館', '日本酒', '本舗', '西日本', '資本', '本場', '本命', '本題', '本業', '日本海', '手本', '本家', '単行本', '本能', '日本初', '日本語版', '本線', '日本政府', '見本市', '日本国内', '本塁打', '見本', '二本', '藤本', '基本法', '本作', '本来なら', '本拠地', '日本史', '本数', '本書', '資本主義', '日本列島', '古本屋', '教育基本法', '文庫本', '日本国民', '本土', '台本', '脚本家', '古本', '日本時間', '本職', '本質的', '本領', '本立て', '本心', '読本', '本位', '日本食', '日本的', '日本国憲法', '三本', '日本共産党', '本堂', '日本軍', '日本料理', '日本企業', '本国', '日本画', '総本山', '本性', '不本意', '日本中', '本島', '本山', '標本', '本腰', '本丸', '日本円', '本部長', '本尊', '大本営', '本流', '本誌', '本宮', '本件', '元本', '本紙', '本木', '二本立て', '四本', '日本銀行', '日本書紀', '本塁', '本学', '本稿', '本庁', '日本電気', '自己資本', '写本', '日本道路公団', '旗本', '本科', '参謀本部', '本省']), ('henshall', 70), ('gsf', 38), ('char', '本'), ('mean', 46), ('count', 17), ('median', 27), ('minimum', 2), ('joyo', True), ('kyoiku_words', ['日本海', '日本料理', '資本家', '日本一', '本分', '興味本位', '不本意', '本体', '日豊本線', '教育基本法', '本宮', '基本料金', '本望', '本番', '日本列島', '製本', '本館', '四本', '台本', '教本', '日本語', '本調子', '日本語版', '本日', '根本的', '本土', '本文', '日本各地', '本学', '本命', '資本', '本職', '日本書紀', '日本道路公団', '日本風', '本家本元', '大本', '全日本', '本義', '本山', '本試験', '見本市', '本業', '本格化', '本州', '本島', '原本', '日本人', '手本', '日本電気', '本箱', '本選', '本会', '日本側', '本件', '本目', '本建築', '本年度', '八本', '本題', '日本初', '写本', '本予算', '本書', '日本全国', '本場所', '副読本', '本領', '本社', '日本食', '本初', '一本化', '版本', '木本', '本丸', '本能', '本', '本場', '本宅', '本式', '本道', '本省', '本営', '基本', '一本道', '本格', '日本文学', '資本金', '本年', '文庫本', '本来', '本部長', '自己資本', '日本紙', '四本柱', '日本円', '本妻', '本則', '日本時間', '見本', '日本軍', '本質的', '本会議', '本局', '旗本', '本意', '総本店', '日本庭園', '標本', '本船', '他力本願', '基本情報', '張本人', '日本社会', '本家', '日本画', '日本中', '日本主義', '本位', '資本主義', '本堂', '日本国民', '本気', '日本車', '本数', '本作', '本庁', '本屋', '新日本製鉄', '本紙', '一本', '基本法', '日本式', '本部', '日本酒', '本案', '日本犬', '日本学術会議', '本署', '本格的', '本店', '三本', '蔵本', '本校', '読本', '日本政府', '本心', '本物', '草本', '日本銀行', '日本製', '本質', '日本語訳', '単行本', '本官', '本当', '絹本', '本木', '本編', '日本茶', '日本', '本隊', '日本史', '本元', '本音', '日本国憲法', '日本原子力研究所', '本性', '社会資本', '配本', '本誌', '本流', '日本的', '総本山', '本科', '日本経済', '本筋', '本人', '日本共産党', '本尊', '本線', '日本刀', '基本的', '本朝', '総本家', '絵本', '根本', '紀勢本線', '西日本', '古本屋', '本有', '大本営', '日本航空', '本格派', '元本', '日本放送協会', '日本国内', '本国', '本願', '本名', '本末', '底本', '二本', '古本'])])
>>> kanji_query = {"$and": [
...         {"char": {"$exists": True}},
...         {"kdict": {"$exists": True}},
...     "$or": [
  File "<stdin>", line 4
    "$or": [
         ^
SyntaxError: invalid syntax
>>>         {"joyo": True},
  File "<stdin>", line 1
    {"joyo": True},
    ^
IndentationError: unexpected indent
>>>         {"kyoiku": True},
  File "<stdin>", line 1
    {"kyoiku": True},
    ^
IndentationError: unexpected indent
>>>         {"heisig": {"$exists": True}},
  File "<stdin>", line 1
    {"heisig": {"$exists": True}},
    ^
IndentationError: unexpected indent
>>>         {"henshall": {"$exists": True}},
  File "<stdin>", line 1
    {"henshall": {"$exists": True}},
    ^
IndentationError: unexpected indent
>>>         {"kklc": {"$exists": True}},
  File "<stdin>", line 1
    {"kklc": {"$exists": True}},
    ^
IndentationError: unexpected indent
>>>         {"rm_rank": {"$lt": 2400}},
  File "<stdin>", line 1
    {"rm_rank": {"$lt": 2400}},
    ^
IndentationError: unexpected indent
>>>         {"kanjidic": {"$lt": 2400}},
  File "<stdin>", line 1
    {"kanjidic": {"$lt": 2400}},
    ^
IndentationError: unexpected indent
>>>         {"mean": {"$lt": 2400}},
  File "<stdin>", line 1
    {"mean": {"$lt": 2400}},
    ^
IndentationError: unexpected indent
>>>         {"rank": {"$lt": 2400}},
  File "<stdin>", line 1
    {"rank": {"$lt": 2400}},
    ^
IndentationError: unexpected indent
>>>         {"freq": {"$lt": 2200}},
  File "<stdin>", line 1
    {"freq": {"$lt": 2200}},
    ^
IndentationError: unexpected indent
>>>         {"variety": {"$lt": 2000}},
  File "<stdin>", line 1
    {"variety": {"$lt": 2000}},
    ^
IndentationError: unexpected indent
>>>         {"wikipedia": {"$lt": 2000}},
  File "<stdin>", line 1
    {"wikipedia": {"$lt": 2000}},
    ^
IndentationError: unexpected indent
>>>         {"top1000words": {"$exists": True}},
  File "<stdin>", line 1
    {"top1000words": {"$exists": True}},
    ^
IndentationError: unexpected indent
>>>         {"top3000words": {"$exists": True}},
  File "<stdin>", line 1
    {"top3000words": {"$exists": True}},
    ^
IndentationError: unexpected indent
>>>         {"top5000words": {"$exists": True}},
  File "<stdin>", line 1
    {"top5000words": {"$exists": True}},
    ^
IndentationError: unexpected indent
>>>         {"top10000words": {"$exists": True}},
  File "<stdin>", line 1
    {"top10000words": {"$exists": True}},
    ^
IndentationError: unexpected indent
>>>         {"top15000words": {"$exists": True}},
  File "<stdin>", line 1
    {"top15000words": {"$exists": True}},
    ^
IndentationError: unexpected indent
>>>         {"top20000words": {"$exists": True}},
  File "<stdin>", line 1
    {"top20000words": {"$exists": True}},
    ^
IndentationError: unexpected indent
>>>         {"top25000words": {"$exists": True}},
  File "<stdin>", line 1
    {"top25000words": {"$exists": True}},
    ^
IndentationError: unexpected indent
>>>         {"novels": {"$lt": 2000}},
  File "<stdin>", line 1
    {"novels": {"$lt": 2000}},
    ^
IndentationError: unexpected indent
>>>         {"blogs": {"$lt": 2000}},
  File "<stdin>", line 1
    {"blogs": {"$lt": 2000}},
    ^
IndentationError: unexpected indent
>>>         {"yatskov_novels": {"$lt": 2000}},
  File "<stdin>", line 1
    {"yatskov_novels": {"$lt": 2000}},
    ^
IndentationError: unexpected indent
>>>         {"aozora": {"$lt": 2000}},
  File "<stdin>", line 1
    {"aozora": {"$lt": 2000}},
    ^
IndentationError: unexpected indent
>>>         {"rm2323": True}
  File "<stdin>", line 1
    {"rm2323": True}
    ^
IndentationError: unexpected indent
>>>     ]
  File "<stdin>", line 1
    ]
    ^
IndentationError: unexpected indent
>>> }
  File "<stdin>", line 1
    }
    ^
SyntaxError: invalid syntax
>>> kanji_query = {"$and": [
...         {"char": {"$exists": True}},
...         {"kdict": {"$exists": True}},
...     "$or": [
  File "<stdin>", line 4
    "$or": [
         ^
SyntaxError: invalid syntax
>>>         {"joyo": True},
  File "<stdin>", line 1
    {"joyo": True},
    ^
IndentationError: unexpected indent
>>>         {"kyoiku": True},
  File "<stdin>", line 1
    {"kyoiku": True},
    ^
IndentationError: unexpected indent
>>>         {"heisig": {"$exists": True}},
  File "<stdin>", line 1
    {"heisig": {"$exists": True}},
    ^
IndentationError: unexpected indent
>>>         {"henshall": {"$exists": True}},
  File "<stdin>", line 1
    {"henshall": {"$exists": True}},
    ^
IndentationError: unexpected indent
>>>         {"kklc": {"$exists": True}},
  File "<stdin>", line 1
    {"kklc": {"$exists": True}},
    ^
IndentationError: unexpected indent
>>>         {"rm_rank": {"$lt": 2400}},
  File "<stdin>", line 1
    {"rm_rank": {"$lt": 2400}},
    ^
IndentationError: unexpected indent
>>>         {"kanjidic": {"$lt": 2400}},
  File "<stdin>", line 1
    {"kanjidic": {"$lt": 2400}},
    ^
IndentationError: unexpected indent
>>>         {"mean": {"$lt": 2400}},
  File "<stdin>", line 1
    {"mean": {"$lt": 2400}},
    ^
IndentationError: unexpected indent
>>>         {"rank": {"$lt": 2400}},
  File "<stdin>", line 1
    {"rank": {"$lt": 2400}},
    ^
IndentationError: unexpected indent
>>>         {"freq": {"$lt": 2200}},
  File "<stdin>", line 1
    {"freq": {"$lt": 2200}},
    ^
IndentationError: unexpected indent
>>>         {"variety": {"$lt": 2000}},
  File "<stdin>", line 1
    {"variety": {"$lt": 2000}},
    ^
IndentationError: unexpected indent
>>>         {"wikipedia": {"$lt": 2000}},
  File "<stdin>", line 1
    {"wikipedia": {"$lt": 2000}},
    ^
IndentationError: unexpected indent
>>>         {"top1000words": {"$exists": True}},
  File "<stdin>", line 1
    {"top1000words": {"$exists": True}},
    ^
IndentationError: unexpected indent
>>>         {"top3000words": {"$exists": True}},
  File "<stdin>", line 1
    {"top3000words": {"$exists": True}},
    ^
IndentationError: unexpected indent
>>>         {"top5000words": {"$exists": True}},
  File "<stdin>", line 1
    {"top5000words": {"$exists": True}},
    ^
IndentationError: unexpected indent
>>>         {"top10000words": {"$exists": True}},
  File "<stdin>", line 1
    {"top10000words": {"$exists": True}},
    ^
IndentationError: unexpected indent
>>>         {"top15000words": {"$exists": True}},
  File "<stdin>", line 1
    {"top15000words": {"$exists": True}},
    ^
IndentationError: unexpected indent
>>>         {"top20000words": {"$exists": True}},
  File "<stdin>", line 1
    {"top20000words": {"$exists": True}},
    ^
IndentationError: unexpected indent
>>>         {"top25000words": {"$exists": True}},
  File "<stdin>", line 1
    {"top25000words": {"$exists": True}},
    ^
IndentationError: unexpected indent
>>>         {"novels": {"$lt": 2000}},
  File "<stdin>", line 1
    {"novels": {"$lt": 2000}},
    ^
IndentationError: unexpected indent
>>>         {"blogs": {"$lt": 2000}},
  File "<stdin>", line 1
    {"blogs": {"$lt": 2000}},
    ^
IndentationError: unexpected indent
>>>         {"yatskov_novels": {"$lt": 2000}},
  File "<stdin>", line 1
    {"yatskov_novels": {"$lt": 2000}},
    ^
IndentationError: unexpected indent
>>>         {"aozora": {"$lt": 2000}},
  File "<stdin>", line 1
    {"aozora": {"$lt": 2000}},
    ^
IndentationError: unexpected indent
>>>         {"rm2323": True}
  File "<stdin>", line 1
    {"rm2323": True}
    ^
IndentationError: unexpected indent
>>>     ]]
  File "<stdin>", line 1
    ]]
    ^
IndentationError: unexpected indent
>>> }
  File "<stdin>", line 1
    }
    ^
SyntaxError: invalid syntax
>>> kanji_query = {"$and": [
...         {"char": {"$exists": True}},
...         {"kdict": {"$exists": True}},
...     {"$or": [
...         {"joyo": True},
...         {"kyoiku": True},
...         {"heisig": {"$exists": True}},
...         {"henshall": {"$exists": True}},
...         {"kklc": {"$exists": True}},
...         {"rm_rank": {"$lt": 2400}},
...         {"kanjidic": {"$lt": 2400}},
...         {"mean": {"$lt": 2400}},
...         {"rank": {"$lt": 2400}},
...         {"freq": {"$lt": 2200}},
...         {"variety": {"$lt": 2000}},
...         {"wikipedia": {"$lt": 2000}},
...         {"top1000words": {"$exists": True}},
...         {"top3000words": {"$exists": True}},
...         {"top5000words": {"$exists": True}},
...         {"top10000words": {"$exists": True}},
...         {"top15000words": {"$exists": True}},
...         {"top20000words": {"$exists": True}},
...         {"top25000words": {"$exists": True}},
...         {"novels": {"$lt": 2000}},
...         {"blogs": {"$lt": 2000}},
...         {"yatskov_novels": {"$lt": 2000}},
...         {"aozora": {"$lt": 2000}},
...         {"rm2323": True}
...             ]
...         }
...     ]
... }
>>> kanji
kanji        kanji_query  kanjidict
>>> kanjidict = {k['char']: k.items() for k in db.kanji.find(kanji_query, proj)}
>>> len(kanjidict)
0
>>> kcur = db.kanji.find(kanji_query, proj)
>>> kanjidict = {k['char']: k.items() for k in kcur}
>>> len(kanji
kanji        kanji_query  kanjidict
>>> len(kanjidict)
0
>>> db.kanji.find(kanji_query).count()
0
>>> kanji_query = {"$and": [
...         {"char": {"$exists": True}},
...         {"kanjidic": {"$exists": True}},
...     {"$or": [
...         {"joyo": True},
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


...         {"kyoiku": True},
...         {"rm2323": True},
...         {"heisig": {"$exists": True}},
...         {"henshall": {"$exists": True}},
...         {"kklc": {"$exists": True}},
...         {"rm_rank": {"$lt": 2400}},
...         {"kanjidic": {"$lt": 2400}},
...         {"mean": {"$lt": 2400}},
...         {"rank": {"$lt": 2400}},
...         {"freq": {"$lt": 2200}},
...         {"variety": {"$lt": 2000}},
...         {"wikipedia": {"$lt": 2000}},
...         {"novels": {"$lt": 2000}},
...         {"blogs": {"$lt": 2000}},
...         {"top1000words": {"$exists": True}},
...         {"top3000words": {"$exists": True}},
...         {"top5000words": {"$exists": True}},
...         {"top10000words": {"$exists": True}},
...         {"top15000words": {"$exists": True}},
...         {"top20000words": {"$exists": True}},
...         {"top25000words": {"$exists": True}},
...         {"twitter": {"$lt": 2000}},
...         {"yatskov_novels": {"$lt": 2000}},
...         {"aozora": {"$lt": 2000}}
...             ]
...         }
...     ]
... }
>>>
>>>
>>>
>>> db.kanji.find(kanji_query).count()
2140
>>> db.kanji.find(kanji_query)kanji_query = {"$and": [.count()
  File "<stdin>", line 1
    db.kanji.find(kanji_query)kanji_query = {"$and": [.count()
                                        ^
SyntaxError: invalid syntax
>>>         {"char": {"$exists": True}},
  File "<stdin>", line 1
    {"char": {"$exists": True}},
    ^
IndentationError: unexpected indent
>>>     {"$or": [
  File "<stdin>", line 1
    {"$or": [
    ^
IndentationError: unexpected indent
>>>         {"joyo": True},
  File "<stdin>", line 1
    {"joyo": True},
    ^
IndentationError: unexpected indent
>>>         {"kyoiku": True},
  File "<stdin>", line 1
    {"kyoiku": True},
    ^
IndentationError: unexpected indent
>>>         {"rm2323": True},
  File "<stdin>", line 1
    {"rm2323": True},
    ^
IndentationError: unexpected indent
>>>         {"heisig": {"$exists": True}},
  File "<stdin>", line 1
    {"heisig": {"$exists": True}},
    ^
IndentationError: unexpected indent
>>>         {"henshall": {"$exists": True}},
  File "<stdin>", line 1
    {"henshall": {"$exists": True}},
    ^
IndentationError: unexpected indent
>>>         {"kklc": {"$exists": True}},
  File "<stdin>", line 1
    {"kklc": {"$exists": True}},
    ^
IndentationError: unexpected indent
>>>         {"rm_rank": {"$lt": 2400}},
  File "<stdin>", line 1
    {"rm_rank": {"$lt": 2400}},
    ^
IndentationError: unexpected indent
>>>         {"kanjidic": {"$lt": 2400}},
  File "<stdin>", line 1
    {"kanjidic": {"$lt": 2400}},
    ^
IndentationError: unexpected indent
>>>         {"mean": {"$lt": 2400}},
  File "<stdin>", line 1
    {"mean": {"$lt": 2400}},
    ^
IndentationError: unexpected indent
>>>         {"rank": {"$lt": 2400}},
  File "<stdin>", line 1
    {"rank": {"$lt": 2400}},
    ^
IndentationError: unexpected indent
>>>         {"freq": {"$lt": 2200}},
  File "<stdin>", line 1
    {"freq": {"$lt": 2200}},
    ^
IndentationError: unexpected indent
>>>         {"variety": {"$lt": 2000}},
  File "<stdin>", line 1
    {"variety": {"$lt": 2000}},
    ^
IndentationError: unexpected indent
>>>         {"wikipedia": {"$lt": 2000}},
  File "<stdin>", line 1
    {"wikipedia": {"$lt": 2000}},
    ^
IndentationError: unexpected indent
>>>         {"novels": {"$lt": 2000}},
  File "<stdin>", line 1
    {"novels": {"$lt": 2000}},
    ^
IndentationError: unexpected indent
>>>         {"blogs": {"$lt": 2000}},
  File "<stdin>", line 1
    {"blogs": {"$lt": 2000}},
    ^
IndentationError: unexpected indent
>>>         {"top1000words": {"$exists": True}},
  File "<stdin>", line 1
    {"top1000words": {"$exists": True}},
    ^
IndentationError: unexpected indent
>>>         {"top3000words": {"$exists": True}},
  File "<stdin>", line 1
    {"top3000words": {"$exists": True}},
    ^
IndentationError: unexpected indent
>>>         {"top5000words": {"$exists": True}},
  File "<stdin>", line 1
    {"top5000words": {"$exists": True}},
    ^
IndentationError: unexpected indent
>>>         {"top10000words": {"$exists": True}},
  File "<stdin>", line 1
    {"top10000words": {"$exists": True}},
    ^
IndentationError: unexpected indent
>>>         {"top15000words": {"$exists": True}},
  File "<stdin>", line 1
    {"top15000words": {"$exists": True}},
    ^
IndentationError: unexpected indent
>>>         {"top20000words": {"$exists": True}},
  File "<stdin>", line 1
    {"top20000words": {"$exists": True}},
    ^
IndentationError: unexpected indent
>>>         {"top25000words": {"$exists": True}},
  File "<stdin>", line 1
    {"top25000words": {"$exists": True}},
    ^
IndentationError: unexpected indent
>>>         {"twitter": {"$lt": 2000}},
  File "<stdin>", line 1
    {"twitter": {"$lt": 2000}},
    ^
IndentationError: unexpected indent
>>>         {"yatskov_novels": {"$lt": 2000}},
  File "<stdin>", line 1
    {"yatskov_novels": {"$lt": 2000}},
    ^
IndentationError: unexpected indent
>>>         {"aozora": {"$lt": 2000}}
  File "<stdin>", line 1
    {"aozora": {"$lt": 2000}}
    ^
IndentationError: unexpected indent
>>>             ]
  File "<stdin>", line 1
    ]
    ^
IndentationError: unexpected indent
>>>         }
  File "<stdin>", line 1
    }
    ^
IndentationError: unexpected indent
>>>     ]
  File "<stdin>", line 1
    ]
    ^
IndentationError: unexpected indent
>>> }
  File "<stdin>", line 1
    }
    ^
SyntaxError: invalid syntax
>>>
>>>
>>> kanji_query = {"$and": [
...         {"char": {"$exists": True}},
...     {"$or": [
...         {"joyo": True},
...         {"kyoiku": True},
...         {"rm2323": True},
...         {"heisig": {"$exists": True}},
...         {"henshall": {"$exists": True}},
...         {"kklc": {"$exists": True}},
...         {"rm_rank": {"$lt": 2400}},
...         {"kanjidic": {"$lt": 2400}},
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


...         {"mean": {"$lt": 2400}},
...         {"rank": {"$lt": 2400}},
...         {"freq": {"$lt": 2200}},
...         {"variety": {"$lt": 2000}},
...         {"wikipedia": {"$lt": 2000}},
...         {"novels": {"$lt": 2000}},
...         {"blogs": {"$lt": 2000}},
...         {"top1000words": {"$exists": True}},
...         {"top3000words": {"$exists": True}},
...         {"top5000words": {"$exists": True}},
...         {"top10000words": {"$exists": True}},
...         {"top15000words": {"$exists": True}},
...         {"top20000words": {"$exists": True}},
...         {"top25000words": {"$exists": True}},
...         {"twitter": {"$lt": 2000}},
...         {"yatskov_novels": {"$lt": 2000}},
...         {"aozora": {"$lt": 2000}}
...             ]
...         }
...     ]
... }
>>>
>>>
>>>
>>> kcur = db.kanji.find(kanji_query, pr)
print(     proj       property(
>>> kcur = db.kanji.find(kanji_query, print(o)
object(  oct(     open(    or       ord(
>>> kcur = db.kanji.find(kanji_query, pro)
proj       property(
>>> kcur = db.kanji.find(kanji_query, proj))
  File "<stdin>", line 1
    kcur = db.kanji.find(kanji_query, proj))
                                           ^
SyntaxError: invalid syntax
>>> kcur = db.kanji.find(kanji_query, proj)
>>> kcur.count()
2754
>>> kanji = {k['char']: k.items() for k in kcur}}
  File "<stdin>", line 1
    kanji = {k['char']: k.items() for k in kcur}}
                                                ^
SyntaxError: invalid syntax
>>> kanji = {k['char']: k.items() for k in kcur}
>>> len(kanji)
2754
>>>

>>> kcur = db.kanji.find(kanji_query, proj))
  File "<stdin>", line 1



























    kcur = db.kanji.find(kanji_query, proj))
                                           ^
SyntaxError: invalid syntax
>>> kcur = db.kanji.find(kanji_query, proj)
>>> kcur.count()
2754
>>> kanji = {k['char']: k.items() for k in kcur}}
  File "<stdin>", line 1
    kanji = {k['char']: k.items() for k in kcur}}
                                                ^
SyntaxError: invalid syntax
>>> kanji = {k['char']: k.items() for k in kcur}
>>> len(kanji)
2754
>>> help(db)

>>> import networkx
>>> help(networkx)

>>> networkx = ''
>>> import networkx as nx













































Help on module cjktools.scripts in cjktools:

NAME
    cjktools.scripts

DESCRIPTION
    This module is responsible for Japanese script/encoding specific methods,
    especially determining the script type of an entry. It is thus the only
    module which requires a utf8 encoding for the additional Japanese characters.

CLASSES
    builtins.object
        Script
        ScriptMapping

    class Script(builtins.object)
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  Ascii = 4
     |
     |  FullAscii = 5
     |
     |  HalfKatakana = 6
     |
     |  Hiragana = 1
     |
     |  Kanji = 3
     |
     |  Katakana = 2
     |
     |  Unknown = 7

    class ScriptMapping(builtins.object)
     |  A mapping function between two scripts. We assume that the given scripts
     |  are different versions of the same characters, and further that they are
     |  aligned at the start and end points stored.
     |
     |  Methods defined here:
     |
     |  __call__(self, j_string)
     |      Converts any matching characters in the given string between scripts.
     |      Any characters which don't match the input script are passed through
     |      unchanged.
     |
     |  __init__(self, from_script, to_script)
     |      Constructor, initializes script conversion.
     |
     |      @param from_script: The script to convert from.
     |      @type from_script: Script
     |      @param to_script: The script to convert to.
     |      @type to_script: Script
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)

FUNCTIONS
    compare_kana(j_string_a, j_string_b)
        Compares two kana strings in a script-independent manner.

            >>> ru_h = u'る'
            >>> ka_h = u'か'
            >>> ka_k = u'カ'
            >>> compare_kana(ru_h, ka_k) == cmp(ru_h, ka_h)
            True

        @type j_string_a: unicode
        @type j_string_b: unicode

    contains_script(script, j_string)
        Returns True if the given script is within the string, False
        otherwise.

            >>> woof = 'woof'
            >>> contains_script(Script.Ascii, woof)
            True
            >>> contains_script(Script.Kanji, woof)
            False

        @param script: The script to search for.
        @type script: Script
        @param j_string: The string to search within.
        @type j_string: unicode

    get_script(script)
        Returns a string containing all charcters in the given script.

    normalize(j_string)
        Jointly normalized full width ascii to single width ascii and half-width
        katakana to full with katakana.

            >>> x = normalize(u'Aあア阿ｱＡ')
            >>> x == u'Aあア阿アA'
            True

        @param j_string: The string to convert.
        @type j_string: unicode
        @return: The converted string.

    normalize_ascii(j_string)
        Normalize a double-width ascii string, converting all characters to
        their single-width counterparts.

        @param j_string: The string to convert.
        @type j_string: unicode
        @return: The converted string.

    normalize_kana(j_string)
        Normalizes all half-width katakana to normal width katakana. Leaves
        all other characters unchanged.

            >>> x = normalize_kana(u'ｶｷｸｹｺ')
            >>> x == u'カキクケコ'
            True

        @param j_string: The string to convert.
        @type j_string: unicode
        @return: The converted string.

    script_boundaries(j_string)
        Determines where the script boundaries are in the given string.

            >>> taberu = u'食べる'
            >>> script_boundaries(taberu) == (taberu[0], taberu[1:])
            True

        @param j_string: The string of Japanese to segment.
        @type j_string: string
        @return: A tuple of script-contiguous blocks

    script_type(char)
        Determine the type of script contained in the given character. Script
        types are expressed using the Script enum.

            >>> woof = 'woof'
            >>> script_types(woof)
            set([Ascii])

>>> help(nx)

>>> help(nx.Graph)

>>> help(nx.weighted)

>>> import cjktools
>>> help(cjktools)

>>> help(cjktools.kanatable)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'cjktools' has no attribute 'kanatable'
>>> help(cjktools.kana_table)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'cjktools' has no attribute 'kana_table'
>>> help(cjktools)

>>> help(cjktools.kana_table)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'cjktools' has no attribute 'kana_table'
>>> help(cjktools)

>>> cjktools.kana_table
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'cjktools' has no attribute 'kana_table'
>>> cjktools.kana_table()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'cjktools' has no attribute 'kana_table'
>>> cjktools
<module 'cjktools' from '/usr/local/lib/python3.6/site-packages/cjktools/__init__.py'>
>>> from cjktools import *
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'cjktools' has no attribute 'enum'
>>> from cjktools import *
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'cjktools' has no attribute 'enum'
>>> from cjktools import scripts
>>> help(scripts)

>>> scripts.get_script(Hiragana)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Hiragana' is not defined
>>> scripts.get_script()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: get_script() missing 1 required positional argument: 'script'
>>> scripts.get_script('Hiragana')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python3.6/site-packages/cjktools/scripts.py", line 152, in get_script
    script_starts, script_ends = _known_bands[script]
KeyError: 'Hiragana'
>>> scripts.get_script('hiragana'))
  File "<stdin>", line 1
    scripts.get_script('hiragana'))
                                  ^
SyntaxError: invalid syntax
>>> scripts.get_script('hiragana')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python3.6/site-packages/cjktools/scripts.py", line 152, in get_script
    script_starts, script_ends = _known_bands[script]
KeyError: 'hiragana'
>>> cjktools = ''
>>> kana = {k.strip() for k in open('Japanese/kana/kana_freq_chars_only.txt').read()}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'Japanese/kana/kana_freq_chars_only.txt'
>>> import os
>>> os.getcwd()
'/Users/ryan/Dropbox/dev/wbtools'
>>> kana = {k.strip() for k in open('kana/kana_freq_chars_only.txt').read()}
>>> kana
{'デ', 'ゲ', 'ら', 'ワ', 'し', 'は', 'み', 'ざ', 'が', 'ぐ', 'ョ', 'ビ', 'か', 'ど', 'に', 'グ', 'ピ', 'ぢ', 'べ', 'ゃ', 'ぷ', 'ぶ', 'じ', 'ゴ', 'せ', 'ォ', 'シ', 'カ', 'コ', 'ぴ', 'モ', 'ぉ', 'ー', 'ム', 'ゥ', 'ヒ', 'タ', 'プ', 'キ', 'ェ', 'レ', 'ゅ', 'ま', 'ュ', 'ぱ', 'ソ', 'ば', 'ね', 'や', 'へ', 'っ', 'び', 'わ', 'ア', 'ズ', 'ベ', 'ぇ', 'う', 'ブ', 'ち', 'ぽ', 'を', 'め', 'ジ', 'ご', 'つ', 'ょ', 'ド', 'す', 'テ', 'フ', 'む', 'ス', 'ヌ', 'ホ', 'だ', 'な', 'て', 'ボ', 'さ', 'メ', 'れ', 'ぬ', 'ギ', 'こ', 'ミ', 'セ', 'ヲ', 'ケ', 'い', 'バ', 'ん', 'イ', 'ず', 'マ', 'ぎ', 'ト', 'パ', 'り', 'げ', 'ぁ', 'サ', 'ほ', 'ヨ', 'あ', 'エ', 'で', 'ウ', 'く', 'ぅ', 'ポ', 'ッ', 'ぼ', 'ャ', 'ラ', 'そ', 'ぞ', 'チ', 'お', 'ザ', 'た', 'ペ', 'ク', 'ヤ', 'ゆ', 'き', 'ひ', 'ぜ', 'ゼ', 'づ', 'ノ', 'ヘ', 'ツ', 'ハ', 'ユ', 'ル', 'リ', 'ロ', 'ふ', 'え', 'ニ', 'と', 'ぺ', 'ダ', 'の', 'ネ', 'ぃ', 'ィ', 'ろ', 'よ', 'ン', 'オ', 'も', 'ガ', 'る', 'ナ', 'け'}
>>> len(kana)
157
>>> def main():
...     katakana = [k.strip() for k in open('Japanese/kana/hiragana_order.txt').read()]
...     hiragana = [k.strip() for k in open('Japanese/kana/katakana_order.txt').read()]
...     kana = set(hiragana) | set(katakana)
...     assert len(kana) > 150
...     return {'hiragana': hiragana, 'katakana': katakana, 'kana': kana}
...
>>> main()
{'hiragana': ['ー', 'ン', 'ル', 'ス', 'ズ', 'ト', 'ド', 'イ', 'ラ', 'フ', 'ブ', 'プ', 'ク', 'グ', 'リ', 'レ', 'ッ', 'ア', 'タ', 'ダ', 'コ', 'ゴ', 'シ', 'ジ', 'マ', 'ヒ', 'ビ', 'ピ', 'ム', 'エ', 'ロ', 'チ', 'ウ', 'テ', 'デ', 'ナ', 'メ', 'カ', 'ニ', 'オ', 'ハ', 'バ', 'パ', 'サ', 'ザ', 'ョ', 'ュ', 'ィ', 'ミ', 'ソ', 'セ', 'ゼ', 'ェ', 'ネ', 'キ', 'ギ', 'ノ', 'ワ', 'ャ', 'ヘ', 'ベ', 'ペ', 'ケ', 'ゲ', 'ガ', 'ツ', 'モ', 'ホ', 'ボ', 'ポ', 'ユ', 'ヤ', 'ォ', 'ゥ', 'ヌ', 'ヨ', 'ヲ', ''], 'katakana': ['あ', 'ぁ', 'い', 'ぃ', 'う', 'ぅ', 'え', 'ぇ', 'お', 'ぉ', 'ん', 'し', 'じ', 'き', 'ぎ', 'に', 'か', 'が', 'の', 'ち', 'ぢ', 'く', 'ぐ', 'と', 'ど', 'は', 'ば', 'ぱ', 'た', 'だ', 'ゆ', 'ゅ', 'こ', 'ご', 'て', 'で', 'さ', 'ざ', 'つ', 'っ', 'づ', 'な', 'せ', 'ぜ', 'る', 'ろ', 'り', 'け', 'げ', 'を', 'よ', 'ょ', 'ら', 'す', 'ず', 'も', 'め', 'ま', 'れ', 'ひ', 'び', 'ぴ', 'ほ', 'ぼ', 'ぽ', 'み', 'そ', 'ぞ', 'ね', 'や', 'ゃ', 'わ', 'ふ', 'ぶ', 'ぷ', 'む', 'へ', 'べ', 'ぺ', 'ぬ', ''], 'kana': {'', 'ス', 'デ', 'ゲ', 'ホ', 'ヌ', 'ら', 'だ', 'な', 'ワ', 'ボ', 'て', 'さ', 'メ', 'し', 'ギ', 'れ', 'は', 'ぬ', 'こ', '













































Help on method add_node in module networkx.classes.graph:

add_node(n, attr_dict=None, **attr) method of networkx.classes.graph.Graph instance
    Add a single node n and update node attributes.

    Parameters
    ----------
    n : node
        A node can be any hashable Python object except None.
    attr_dict : dictionary, optional (default= no attributes)
        Dictionary of node attributes.  Key/value pairs will
        update existing data associated with the node.
    attr : keyword arguments, optional
        Set or change attributes using key=value.

    See Also
    --------
    add_nodes_from

    Examples
    --------
    >>> G = nx.Graph()   # or DiGraph, MultiGraph, MultiDiGraph, etc
    >>> G.add_node(1)
    >>> G.add_node('Hello')
    >>> K3 = nx.Graph([(0,1),(1,2),(2,0)])
    >>> G.add_node(K3)
    >>> G.number_of_nodes()
    3

    Use keywords set/change node attributes:

    >>> G.add_node(1,size=10)
    >>> G.add_node(3,weight=0.4,UTM=('13S',382871,3972649))

    Notes
    -----
    A hashable object is one that can be used as a key in a Python
    dictionary. This includes strings, numbers, tuples of strings
    and numbers, etc.

    On many platforms hashable items also include mutables such as
    NetworkX Graphs, though one should be careful that the hash
    doesn't change on mutables.
...skipping...
ミ', 'セ', 'ヲ', 'ケ', 'い', 'バ', 'み', 'イ', 'ん', 'ざ', 'マ', 'ず', 'ト', 'ぎ', 'が', 'パ', 'ぐ', 'ョ', 'ビ', 'り', 'ぁ', 'か', 'グ', 'ピ', 'サ', 'に', 'ど', 'げ', 'ほ', 'ぢ', 'べ', 'ヨ', 'あ', 'エ', 'で', 'ゃ', 'ウ', 'く', 'ぅ', 'ぷ', 'ぶ', 'じ', 'ポ', 'ゴ', 'ォ', 'せ', 'ッ', 'シ', 'ぼ', 'ャ', 'カ', 'ラ', 'コ', 'ぴ', 'モ', 'ぉ', 'ー', 'ム', 'ぞ', 'そ', 'ゥ', 'ヒ', 'チ', 'プ', 'タ', 'ザ', 'キ', 'お', 'た', 'ェ', 'ペ', 'ク', 'ヤ', 'レ', 'ゅ', 'ま', 'ュ', 'ゆ', 'き', 'ひ', 'ぱ', 'ぜ', 'ソ', 'ゼ', 'ば', 'づ', 'ノ', 'ね', 'ヘ', 'や', 'へ', 'ツ', 'ハ', 'っ', 'ユ', 'リ', 'ル', 'び', 'ロ', 'わ', 'ふ', 'ア', 'ニ', 'え', 'ズ', 'と', 'ベ', 'ぇ', 'う', 'ぺ', 'ダ', 'ブ', 'の', 'ネ', 'ち', 'ぽ', 'ぃ', 'ジ', 'を', 'め', 'ご', 'ド', 'つ', '













































Help on method add_node in module networkx.classes.graph:

add_node(n, attr_dict=None, **attr) method of networkx.classes.graph.Graph instance
    Add a single node n and update node attributes.

    Parameters
    ----------
    n : node
        A node can be any hashable Python object except None.
    attr_dict : dictionary, optional (default= no attributes)
        Dictionary of node attributes.  Key/value pairs will
        update existing data associated with the node.
    attr : keyword arguments, optional
        Set or change attributes using key=value.

    See Also
    --------
    add_nodes_from

    Examples
    --------
    >>> G = nx.Graph()   # or DiGraph, MultiGraph, MultiDiGraph, etc
    >>> G.add_node(1)
    >>> G.add_node('Hello')
    >>> K3 = nx.Graph([(0,1),(1,2),(2,0)])
    >>> G.add_node(K3)
    >>> G.number_of_nodes()
    3

    Use keywords set/change node attributes:

    >>> G.add_node(1,size=10)
    >>> G.add_node(3,weight=0.4,UTM=('13S',382871,3972649))

    Notes
    -----
    A hashable object is one that can be used as a key in a Python
    dictionary. This includes strings, numbers, tuples of strings
    and numbers, etc.

    On many platforms hashable items also include mutables such as
    NetworkX Graphs, though one should be careful that the hash
    doesn't change on mutables.
...skipping...
ィ', 'ょ', 'ろ', 'よ', 'ン', 'す', 'む', 'オ', 'ガ', 'も', 'る', 'テ', 'ナ', 'け', 'フ'}}
>>> kana













































{'デ', 'ゲ', 'ら', 'ワ', 'し', 'は', 'み', 'ざ', 'が', 'ぐ', 'ョ', 'ビ', 'か', 'ど', 'に', 'グ', 'ピ', 'ぢ', 'べ', 'ゃ', 'ぷ', 'ぶ', 'じ', 'ゴ', 'せ', 'ォ', 'シ', 'カ', 'コ', 'ぴ', 'モ', 'ぉ', 'ー', 'ム', 'ゥ', 'ヒ', 'タ', 'プ', 'キ', 'ェ', 'レ', 'ゅ', 'ま', 'ュ', 'ぱ', 'ソ', 'ば', 'ね', 'や', 'へ', 'っ', 'び', 'わ', 'ア', 'ズ', 'ベ', 'ぇ', 'う', 'ブ', 'ち', 'ぽ', 'を', 'め', 'ジ', 'ご', 'つ', 'ょ', 'ド', 'す', 'テ', 'フ', 'む', 'ス', 'ヌ', 'ホ', 'だ', 'な', 'て', 'ボ', 'さ', 'メ', 'れ', 'ぬ', 'ギ', 'こ', 'ミ', 'セ', 'ヲ', 'ケ', 'い', 'バ', 'ん', 'イ', 'ず', 'マ', 'ぎ', 'ト', 'パ', 'り', 'げ', 'ぁ', 'サ', 'ほ', 'ヨ', 'あ', 'エ', 'で', 'ウ', 'く', 'ぅ', 'ポ', 'ッ', 'ぼ', 'ャ', 'ラ', 'そ', 'ぞ', 'チ', 'お', 'ザ', 'た', 'ペ', 'ク', 'ヤ', 'ゆ', 'き', 'ひ', 'ぜ', 'ゼ', 'づ', 'ノ', 'ヘ', 'ツ', 'ハ', 'ユ', 'ル', 'リ', 'ロ', 'ふ', 'え', 'ニ', 'と', 'ぺ', 'ダ', 'の', 'ネ', 'ぃ', 'ィ', 'ろ', 'よ', 'ン', 'オ', 'も', 'ガ', 'る', 'ナ', 'け'}
>>> k2 = main()
>>> type(k2)
<class 'dict'>
>>> len(k2.hiragana)













































Help on dict object:
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>













































Help on Graph in module networkx.classes.graph object:

class Graph(builtins.object)
 |  Base class for undirected graphs.
 |
 |  A Graph stores nodes and edges with optional data, or attributes.
 |
 |  Graphs hold undirected edges.  Self loops are allowed but multiple
 |  (parallel) edges are not.
 |
 |  Nodes can be arbitrary (hashable) Python objects with optional
 |  key/value attributes.
 |
 |  Edges are represented as links between nodes with optional
 |  key/value attributes.
 |
 |  Parameters
 |  ----------
 |  data : input graph
 |      Data to initialize graph.  If data=None (default) an empty
 |      graph is created.  The data can be an edge list, or any
 |      NetworkX graph object.  If the corresponding optional Python
 |      packages are installed the data can also be a NumPy matrix
 |      or 2d ndarray, a SciPy sparse matrix, or a PyGraphviz graph.
 |
 |  attr : keyword arguments, optional (default= no attributes)
 |      Attributes to add to graph as key=value pairs.
 |
 |  See Also
 |  --------
 |  DiGraph
 |  MultiGraph
 |  MultiDiGraph
 |
 |  Examples
 |  --------
 |  Create an empty graph structure (a "null graph") with no nodes and
 |  no edges.
 |
 |  >>> G = nx.Graph()
 |
 |  G can be grown in several ways.
 |
 |  **Nodes:**
 |
 |  Add one node at a time:
 |
 |  >>> G.add_node(1)
 |
 |  Add the nodes from any container (a list, dict, set or
 |  even the lines from a file or the nodes from another graph).
 |
 |  >>> G.add_nodes_from([2,3])
 |  >>> G.add_nodes_from(range(100,110))
 |  >>> H=nx.Graph()
 |  >>> H.add_path([0,1,2,3,4,5,6,7,8,9])
 |  >>> G.add_nodes_from(H)
 |
AttributeError: 'dict' object has no attribute 'hiragana'
>>> len(k2['hiragana'])
78
>>> len(k2['kana'])
158
>>> kanji['脚']
dict_items([('radicals', ['月', '土', '卩', '厶']), ('rm_rank', 1090), ('yatskov_novels', 1012), ('onyomi', ['カク', 'キャ', 'キャク']), ('top3000words', ['脚']), ('freq', 1228), ('radical_list', '脚'), ('hanja', '각'), ('wikipedia', 643), ('kunyomi', ['あし']), ('jlpt', 1), ('pinyin', 'jue2'), ('average', 1145), ('grade', 8), ('kklc', 734), ('novels', 1070), ('variety', 1108), ('mainichi', 1230), ('rm2323', True), ('components', ['⺼', '月', '土', '卩', '厶', '却', '去']), ('kanjidic', 1228), ('kic', 1612), ('twitter', 1285), ('rank', 1133), ('peers', ['胃', '脅', '腐', '肌', '肝', '肥', '肺', '胆', '胞', '脂', '脇', '脈', '腰', '臓', '却', '較', '獲', '核', '鶴']), ('heisig', 1498), ('aozora', 980), ('blogs', 1144), ('rtk_two_examples', 653), ('stroke_count', 11), ('top15000words', ['脚本', '三脚', '脚本家', '脚色', '二人三脚', '失脚', '両脚']), ('henshall', 1146), ('gsf', 1080), ('joyo', True), ('char', '脚'), ('mean', 1102), ('count', 17), ('median', 1108), ('minimum', 643)])
>>> help(G.add_node)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'G' is not defined
>>> nx
<module 'networkx' from '/usr/local/lib/python3.6/site-packages/networkx/__init__.py'>
>>> G = nx.Graph()
>>> help(G.add_node)

>>> help(G.add_nodes)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Graph' object has no attribute 'add_nodes'
>>> help(G.add_node)

>>> help(G.add_nodes_from)

>>> G.add_no
G.add_node(        G.add_nodes_from(
>>> G.add_node('脚')
>>> G
<networkx.classes.graph.Graph object at 0x11ed5de10>
>>> help(G.'脚')
  File "<stdin>", line 1
    help(G.'脚')
             ^
SyntaxError: invalid syntax
>>> help(G['脚'])

>>> help(G)

>>> G.add_node('脚', 'radicals'=kanji['脚']['radicals'])
  File "<stdin>", line 1
SyntaxError: keyword can't be an expression
>>> radicals=kanji['脚']['radicals']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'dict_items' object is not subscriptable
>>> type(kanji['脚'])
<class 'dict_items'>
>>> type(kanji['脚']['radicals'])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'dict_items' object is not subscriptable
>>> def make_kanji_dict():
...     kcur = db.kanji.find(kanji_query, proj)
...     kanji = {k['char']: k for k in kcur}
...     return kanji
...
>>> kanji = make_kanji_dict()
>>> len(kanji)
2754
>>> radicals=kanji['脚']['radicals']
>>> radicals
['月', '土', '卩', '厶']
>>> G.add_node('脚', 'radicals'=radicals)
  File "<stdin>", line 1
SyntaxError: keyword can't be an expression
>>> G.add_node('脚', radicals=radicals)
>>> G.graph()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'dict' object is not callable
>>> G.graph
{}
>>> G
<networkx.classes.graph.Graph object at 0x11ed5de10>
>>> G.nodes
<bound method Graph.nodes of <networkx.classes.graph.Graph object at 0x11ed5de10>>
>>> G.nodes()
['脚']
>>> G['脚']['radicals'] = radicals
>>> G
<networkx.classes.graph.Graph object at 0x11ed5de10>
>>> G.nodes()
['脚']
>>> G.graph()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'dict' object is not callable
>>> G.graph
{}
>>> G['脚']
{'radicals': ['月', '土', '卩', '厶']}
>>> kanji['脚'].keys()
dict_keys(['radicals', 'rm_rank', 'yatskov_novels', 'onyomi', 'top3000words', 'freq', 'radical_list', 'hanja', 'wikipedia', 'kunyomi', 'jlpt', 'pinyin', 'average', 'grade', 'kklc', 'novels', 'variety', 'mainichi', 'rm2323', 'components', 'kanjidic', 'kic', 'twitter', 'rank', 'peers', 'heisig', 'aozora', 'blogs', 'rtk_two_examples', 'stroke_count', 'top15000words', 'henshall', 'gsf', 'joyo', 'char', 'mean', 'count', 'median', 'minimum'])
>>> 'rank' in kanji['脚'].keys()
True
>>> kanji['上'].keys()
dict_keys(['radicals', 'rm_rank', 'yatskov_novels', 'onyomi', 'top3000words', 'freq', 'radical_list', 'hanja', 'wikipedia', 'kunyomi', 'jlpt', 'pinyin', 'average', 'grade', 'kyoiku', 'kklc', 'novels', 'variety', 'mainichi', 'rm2323', 'components', 'kanjidic', 'kic', 'twitter', 'rank', 'peers', 'heisig', 'aozora', 'blogs', 'rtk_two_examples', 'stroke_count', 'top15000words', 'henshall', 'gsf', 'char', 'mean', 'count', 'median', 'minimum', 'joyo', 'kyoiku_words'])
>>> def add_nodes(G):
...     for k in kanji.keys():
...         attribs = kanji[k].keys()
...         G.add_node(k)
...         for a in ['radicals', 'peers', 'onyomi', 'kunyomi', 'grade', 'components',
...         'stroke_count', 'top1000words', 'top3000words', 'top5000words', 'top10000words',
...         'top15000words', 'top20000words', 'top30000words', 'top50000words', 'kyoiku_words',
...         'pinyin', 'jlpt', 'kic', 'kklc', 'heisig', 'kyoiku', 'joyo', 'jinmeiyo']:
...             if a in attribs:
...                 G[k][a] = kanji[k][a]
...     return G
...
>>> G = add_nodes(G)
>>> G
<networkx.classes.graph.Graph object at 0x11ed5de10>
>>> G.graph()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'dict' object is not callable
>>> G.graph
{}
>>> G.nodes
<bound method Graph.nodes of <networkx.classes.graph.Graph object at 0x11ed5de10>>
>>> G.nodes()
['脚', '一', '丁', '七', '万', '丈', '三', '上', '下', '不', '与', '丑', '且', '世', '丘', '丙', '丞', '両', '並', '中', '串', '丸', '丹', '主', '丼', '乃', '乄', '久', '之', '乎', '乏', '乗', '乙', '九', '乞', '也', '乱', '乳', '乾', '亀', '亂', '了', '予', '争', '事', '二', '云', '互', '五', '井', '亘', '亜', '亡', '交', '亥', '亦', '亨', '享', '京', '亭', '亮', '人', '仁', '仄', '今', '介', '仏', '仔', '仕', '他', '付', '仙', '代', '令', '以', '仮', '仰', '仲', '件', '任', '企', '伊', '伍', '伎', '伏', '伐', '休', '会', '伝', '伯', '伴', '伸', '伺', '似', '伽', '佃', '但', '位', '低', '住', '佐', '体', '何', '余', '佛', '作', '佳', '併', '使', '來', '例', '侍', '供', '依', '価', '侮', '侯', '侵', '侶', '便', '係', '促', '俊', '俗', '保', '信', '俣', '修', '俳', '俵', '俸', '俺', '倉', '個', '倍', '倒', '候', '借', '倣', '値', '倦', '倫', '倭', '倶', '倹', '偉', '偏', '停', '健', '偲', '側', '偵', '偶', '偽', '傍', '傑', '傘', '備', '催', '傭', '傲', '傳', '債', '傷', '傾', '僅', '働', '像', '僑', '僕', '僚', '僧', '僻', '儀', '億', '儒', '償', '優', '允', '元', '兄', '充', '兆', '兇', '先', '光', '克', '免', '兎', '児', '党', '兜', '入', '全', '八', '公', '六', '共', '兵', '其', '具', '典', '兼', '内', '円', '冊', '再', '冒', '冗', '写', '冠', '冥', '冬', '冴', '冶', '冷', '凄', '准', '凌', '凍', '凝', '几', '凡', '処', '凪', '凱', '凶', '凸', '凹', '出', '函', '刀', '刃', '分', '切', '刈', '刊', '刑', '列', '初', '判', '別', '利', '到', '制', '刷', '券', '刹', '刺', '刻', '則', '削', '前', '剖', '剛', '剝', '剣', '剤', '剥', '剪', '副', '剰', '割', '創', '劇', '劉', '力', '功', '加', '劣', '助', '努', '励', '労', '効', '劾', '勁', '勃', '勅', '勇', '勉', '動', '勘', '務', '勝', '勞', '募', '勢', '勤', '勧', '勲', '勺', '勾', '勿', '匁', '匂', '包', '匕', '化', '北', '匠', '匡', '匹', '区', '医', '匿', '十', '千', '升', '午', '半', '卑', '卒', '卓', '協', '南', '単', '博', '卜', '占', '卯', '印', '危', '即', '却', '卵', '卸', '卿', '厄', '厖', '厘', '厚', '原', '厨', '厭', '厳', '去', '参', '參', '又', '叉', '及', '友', '双', '反', '収', '叔', '取', '受', '叙', '叛', '叡', '叢', '口', '古', '句', '只', '叫', '召', '可', '台', '叱', '史', '右', '叶', '号', '司', '吃', '各', '合', '吉', '吊', '同', '名', '后', '吏', '吐', '向', '君', '吟', '否', '含', '吸', '吹', '吾', '呂', '呈', '呉', '告', '呑', '周', '呪', '味', '呼', '命', '和', '咲', '咽', '哀', '品', '哉', '員', '哲', '哺', '唄', '唆', '唇', '唐', '唯', '唱', '唾', '商', '問', '啓', '善', '喉', '喚', '喜', '喝', '喧', '喩', '喪', '喫', '喬', '單', '喰', '営', '嗅', '嗣', '嘆', '嘉', '嘘', '嘱', '嘲', '器', '噴', '嚇', '囚', '四', '回', '因', '団', '困', '囲', '図', '固', '国', '圃', '國', '圍', '圏', '園', '圓', '圖', '土', '圧', '在', '圭', '地', '坂', '均', '坊', '坐', '坑', '坦', '坪', '垂', '型', '垢', '垣', '埋', '城', '域', '埴', '執', '培', '基', '埼', '堀', '堂', '堅', '堆', '堕', '堤', '堪', '報', '場', '堺', '塀', '塁', '塊', '塑', '塔', '塗', '塚', '塞', '塡', '塩', '塵', '塾', '境', '墓', '増', '墜', '墨', '墳', '墾', '壁', '壇', '壊', '壌', '壕', '士', '壬', '壮', '声', '壱', '売', '壽', '変', '夏', '夕', '外', '多', '夜', '夢', '大', '天', '太', '夫', '央', '失', '夷', '奄', '奇', '奈', '奉', '奎', '奏', '契', '奔', '奥', '奨', '奪', '奮', '女', '奴', '好', '如', '妃', '妄', '妊', '妖', '妙', '妥', '妨', '妬', '妹', '妻', '姉', '始', '姓', '委', '姥', '姫', '姻', '姿', '威', '娘', '娠', '娯', '婆', '婉', '婚', '婦', '婿', '媒', '媛', '嫁', '嫉', '嫌', '嫡', '嬉', '嬌', '嬢', '子', '孔', '孕', '字', '存', '孜', '孝', '孟', '季', '孤', '学', '孫', '宅', '宇', '守', '安', '宋', '完', '宏', '宗', '官', '宙', '定', '宛', '宜', '宝', '実', '客', '宣', '室', '宥', '宮', '宰', '害', '宴', '宵', '家', '容', '宿', '寂', '寄', '寅', '密', '富', '寒', '寛', '寝', '察', '寡', '實', '寧', '審', '寮', '寵', '寸', '寺', '対', '寿', '封', '専', '射', '将', '尉', '尊', '尋', '導', '小', '少', '尖', '尚', '尤', '尭', '就', '尺', '尻', '尼', '尽', '尾', '尿', '局', '居', '屈', '届', '屋', '屍', '展', '属', '層', '履', '屯', '山', '岐', '岡', '岩', '岬', '岳', '岸', '峠', '峡', '峨', '峯', '峰', '島', '峻', '崇', '崎', '崖', '崩', '嵌', '嵐', '嵯', '嶋', '嶺', '嶽', '巌', '川', '州', '巡', '巣', '工', '左', '巧', '巨', '巫', '差', '己', '已', '巳', '巴', '巻', '巽', '巾', '市', '布', '帆', '希', '帖', '帝', '帥', '師', '席', '帯', '帰', '帳', '帶', '常', '帽', '幅', '幌', '幕', '幟', '幡', '幣', '干', '平', '年', '幸', '幹', '幻', '幼', '幽', '幾', '庁', '広', '庄', '床', '序', '底', '庖', '店', '庚', '府', '度', '座', '庫', '庭', '庵', '庶', '康', '庸', '廃', '廉', '廊', '廓', '廣', '延', '廷', '建', '廻', '廿', '弁', '弄', '弊', '式', '弐', '弓', '弔', '引', '弘', '弟', '弥', '弦', '弧', '弱', '張', '強', '弾', '彌', '当', '彗', '彙', '形', '彦', '彩', '彫', '彬', '彰', '影', '役', '彼', '往', '征', '径', '待', '律', '後', '徐', '徒', '従', '得', '從', '御', '復', '循', '微', '徳', '徴', '徹', '徽', '心', '必', '忌', '忍', '志', '忘', '忙', '応', '忠', '快', '念', '忽', '怒', '怖', '思', '怠', '急', '性', '怨', '怪', '恋', '恐', '恒', '恢', '恣', '恥', '恨', '恩', '恭', '息', '恰', '恵', '悉', '悔', '悟', '悠', '患', '悦', '悩', '悪', '悲', '悼', '情', '惑', '惜', '惟', '惡', '惣', '惧', '惨', '惰', '想', '惹', '愁', '愉', '意', '愚', '愛', '感', '慄', '慈', '態', '慌', '慎', '慕', '慢', '慣', '慧', '慨', '慮', '慰', '慶', '慾', '憂', '憎', '憐', '憑', '憤', '憧', '憩', '憬', '憲', '憶', '憾', '懇', '應', '懐', '懲', '懷', '懸', '戀', '戌', '成', '我', '戒', '或', '戚', '戦', '截', '戯', '戴', '戸', '戻', '房', '所', '扇', '扉', '手', '才', '打', '払', '扱', '扶', '批', '承', '技', '抄', '把', '抑', '投', '抗', '折', '抜', '択', '披', '抱', '抵', '抹', '押', '抽', '担', '拉', '拍', '拐', '拒', '拓', '拘', '拙', '招', '拝', '拠', '拡', '括', '拭', '拳', '拶', '拷', '拾', '持', '指', '按', '挑', '挙', '挟', '挨', '挫', '振', '挺', '挽', '挿', '捉', '捕', '捗', '捜', '捧', '捨', '据', '捷', '捻', '掃', '授', '掌', '排', '掘', '掛', '掠', '採', '探', '接', '控', '推', '措', '掲', '掴', '揃', '揆', '描', '提', '揚', '換', '握', '揮', '援', '揺', '損', '搬', '搭', '携', '搾', '摂', '摘', '摩', '摯', '摺', '撃', '撒', '撤', '播', '撮', '撲', '擁', '操', '擦', '擧', '擬', '支', '改', '攻', '放', '政', '故', '敏', '救', '敗', '教', '敢', '散', '敦', '敬', '数', '整', '敵', '敷', '數', '文', '斉', '斎', '斐', '斑', '斗', '料', '斜', '斤', '斥', '斧', '斬', '断', '斯', '新', '斷', '方', '於', '施', '旅', '旋', '族', '旗', '既', '日', '旦', '旧', '旨', '早', '旬', '旭', '旱', '旺', '昂', '昆', '昇', '昌', '明', '昏', '易', '昔', '星', '映', '春', '昧', '昨', '昭', '是', '昼', '時', '晃', '晋', '晩', '普', '景', '晴', '晶', '智', '暁', '暇', '暈', '暑', '暖', '暗', '暢', '暦', '暫', '暮', '暴', '曇', '曖', '曙', '曜', '曝', '曠', '曰', '曲', '更', '書', '曹', '曼', '曽', '替', '最', '會', '月', '有', '朋', '服', '朔', '朕', '朗', '望', '朝', '期', '木', '未', '末', '本', '札', '朱', '朴', '机', '朽', '杉', '李', '杏', '材', '村', '杓', '杖', '杜', '束', '条', '来', '杯', '東', '杵', '杷', '松', '板', '析', '枕', '林', '枚', '果', '枝', '枠', '枢', '枯', '架', '柄', '柊', '柏', '某', '柑', '染', '柔', '柘', '柚', '柱', '柳', '柴', '柵', '査', '柿', '栃', '栄', '栓', '栖', '栗', '栞', '校', '株', '核', '根', '格', '栽', '桁', '桂', '桃', '案', '桐', '桑', '桜', '桟', '桶', '梁', '梅', '梓', '梗', '梢', '梧', '梨', '梯', '械', '梵', '梶', '棄', '棋', '棒', '棚', '棟', '森', '棲', '棺', '椀', '椅', '植', '椎', '検', '椰', '椿', '楊', '楓', '楠', '楢', '業', '楯', '極', '楷', '楼', '楽', '概', '榊', '榎', '榛', '構', '槌', '槍', '様', '槙', '槻', '槽', '樋', '標', '模', '権', '横', '樹', '樺', '樽', '橋', '橘', '機', '橿', '檀', '檜', '櫛', '櫻', '欄', '權', '欝', '欠', '次', '欣', '欧', '欲', '欺', '欽', '款', '歌', '歎', '歓', '止', '正', '此', '武', '歩', '歯', '歳', '歴', '歸', '死', '殉', '殊', '残', '殖', '殴', '段', '殺', '殻', '殿', '毀', '毅', '母', '毎', '毒', '比', '毛', '氏', '民', '気', '氣', '水', '氷', '永', '氾', '汁', '求', '汎', '汐', '汗', '汚', '江', '池', '汰', '汲', '決', '汽', '沃', '沈', '沓', '沖', '沙', '没', '沢', '沫', '河', '沸', '油', '治', '沼', '沿', '況', '泉', '泊', '泌', '法', '泡', '波', '泣', '泥', '注', '泰', '泳', '洋', '洒', '洗', '洛', '洞', '津', '洪', '洲', '活', '派', '流', '浄', '浅', '浜', '浦', '浩', '浪', '浮', '浴', '海', '浸', '消', '涙', '涯', '液', '涼', '淀', '淋', '淑', '淡', '淫', '深', '淳', '淵', '混', '添', '清', '渇', '済', '渉', '渋', '渓', '渚', '減', '渡', '渦', '温', '測', '港', '渾', '湊', '湖', '湛', '湧', '湯', '湾', '湿', '満', '溌', '源', '準', '溜', '溝', '溪', '溶', '溺', '滅', '滋', '滑', '滝', '滞', '滲', '滴', '漁', '漂', '漆', '漏', '演', '漕', '漠', '漢', '漫', '漬', '漱', '漸', '潔', '潜', '潟', '潤', '潮', '潰', '澄', '澤', '澱', '激', '濁', '濃', '濟', '濠', '濫', '濯', '瀕', '瀧', '瀬', '灘', '火', '灯', '灰', '災', '炉', '炊', '炎', '炭', '点', '為', '烈', '烏', '焔', '焚', '無', '焦', '然', '焼', '煉', '煎', '煕', '煙', '照', '煩', '煮', '煽', '熊', '熔', '熟', '熱', '燃', '燈', '燒', '燕', '燥', '爆', '爛', '爪', '爲', '爵', '父', '爽', '爾', '片', '版', '牒', '牙', '牛', '牝', '牟', '牡', '牧', '物', '牲', '特', '牽', '犀', '犠', '犬', '犯', '状', '狂', '狐', '狗', '狙', '狛', '狩', '独', '狭', '狼', '猛', '猟', '猪', '猫', '献', '猶', '猾', '猿', '獄', '獅', '獣', '獨', '獲', '玄', '率', '玉', '王', '玖', '玩', '玲', '珊', '珍', '珠', '班', '現', '球', '理', '琉', '琢', '琴', '瑚', '瑞', '瑠', '璃', '璧', '環', '璽', '瓜', '瓢', '瓣', '瓦', '瓶', '甘', '甚', '生', '産', '甦', '用', '田', '由', '甲', '申', '男', '町', '画', '界', '畏', '畑', '畔', '留', '畜', '畝', '畠', '略', '畦', '番', '畫', '異', '畳', '當', '畿', '疋', '疎', '疏', '疑', '疫', '疲', '疾', '病', '症', '痔', '痕', '痘', '痛', '痢', '痩', '痴', '瘍', '療', '癒', '癖', '発', '登', '發', '白', '百', '的', '皆', '皇', '皐', '皮', '皿', '盆', '益', '盗', '盛', '盟', '盡', '監', '盤', '目', '盲', '直', '相', '盾', '省', '眉', '看', '県', '眞', '真', '眠', '眸', '眺', '眼', '着', '睡', '督', '睦', '瞬', '瞭', '瞳', '矛', '矢', '知', '短', '矯', '石', '砂', '研', '砕', '砥', '砦', '砲', '破', '硝', '硫', '硬', '硯', '碁', '碇', '碑', '碧', '確', '磁', '磐', '磨', '磯', '礁', '礎', '示', '礼', '社', '祀', '祇', '祈', '祉', '祐', '祓', '祖', '祝', '神', '祢', '祥', '票', '祭', '祷', '禁', '禄', '禅', '禍', '禎', '福', '禦', '禮', '禿', '秀', '私', '秋', '科', '秒', '秘', '租', '秦', '秩', '称', '移', '稀', '程', '税', '稔', '稗', '稚', '稜', '種', '稱', '稲', '稼', '稽', '稿', '穀', '穂', '積', '穎', '穏', '穫', '穴', '究', '空', '穿', '突', '窃', '窒', '窓', '窟', '窪', '窮', '窯', '立', '竜', '章', '竣', '童', '竪', '端', '競', '竹', '竺', '笈', '笑', '笛', '笠', '笥', '符', '第', '笹', '筆', '等', '筋', '筏', '筑', '筒', '答', '策', '箇', '箋', '箕', '算', '管', '箭', '箱', '箸', '節', '範', '篇', '築', '篠', '篤', '簡', '簾', '簿', '籍', '籠', '米', '籾', '粉', '粋', '粒', '粗', '粘', '粛', '粟', '粧', '精', '糊', '糖', '糠', '糧', '糸', '系', '糾', '紀', '約', '紅', '紋', '納', '紐', '純', '紗', '紘', '紙', '級', '紛', '素', '紡', '索', '紫', '累', '細', '紳', '紹', '紺', '終', '絃', '組', '経', '結', '絞', '絡', '給', '統', '絵', '絶', '絹', '継', '続', '綜', '綬', '維', '綱', '網', '綴', '綸', '綺', '綻', '綾', '綿', '緊', '緋', '総', '緑', '緒', '線', '締', '編', '緩', '緯', '練', '緻', '縁', '縄', '縛', '縦', '縫', '縮', '績', '繁', '繊', '繋', '繍', '織', '繕', '繩', '繪', '繭', '繰', '續', '纏', '缶', '罪', '置', '罰', '署', '罵', '罷', '羅', '羊', '美', '羞', '群', '羨', '義', '羽', '翁', '翌', '習', '翔', '翠', '翰', '翻', '翼', '老', '考', '者', '而', '耐', '耕', '耗', '耳', '耶', '聖', '聚', '聞', '聡', '聯', '聲', '聴', '職', '肇', '肉', '肌', '肖', '肘', '肛', '肝', '股', '肢', '肥', '肩', '肪', '肯', '育', '肴', '肺', '胃', '胆', '背', '胎', '胞', '胡', '胴', '胸', '能', '脂', '脅', '脇', '脈', '脊', '脱', '脳', '脹', '腎', '腐', '腕', '腫', '腰', '腸', '腹', '腺', '膏', '膚', '膜', '膝', '膨', '膳', '臆', '臓', '臣', '臥', '臨', '自', '臭', '至', '致', '臺', '臼', '與', '興', '舌', '舎', '舗', '舞', '舟', '航', '般', '舶', '舷', '船', '艇', '艦', '艮', '良', '色', '艶', '芋', '芙', '芝', '芥', '芦', '芭', '芯', '花', '芳', '芸', '芹', '芽', '苅', '苑', '苔', '苗', '苛', '若', '苦', '苫', '英', '茂', '茄', '茅', '茉', '茎', '茜', '茨', '茶', '茸', '草', '荒', '荘', '荷', '荻', '莉', '莫', '菅', '菊', '菌', '菓', '菜', '華', '菰', '菱', '萌', '萎', '萩', '萬', '落', '葉', '著', '葛', '葡', '葦', '葬', '葵', '葺', '蒐', '蒔', '蒙', '蒲', '蒸', '蒼', '蓄', '蓉', '蓋', '蓑', '蓬', '蓮', '蔑', '蔓', '蔦', '蔭', '蔵', '蔽', '蕃', '蕉', '蕨', '蕪', '薄', '薦', '薩', '薪', '薫', '薬', '藁', '藍', '藝', '藤', '藩', '藻', '蘇', '蘭', '虎', '虐', '虔', '處', '虚', '虜', '虞', '虫', '虹', '蚊', '蚕', '蛇', '蛍', '蛙', '蛤', '蛭', '蛮', '蜂', '蜜', '蝕', '蝦', '蝶', '融', '螺', '蟹', '蟻', '血', '衆', '行', '術', '街', '衛', '衝', '衡', '衣', '表', '衰', '衷', '衿', '袈', '袋', '袖', '被', '袴', '裁', '裂', '装', '裏', '裕', '補', '裟', '裡', '裳', '裸', '製', '裾', '複', '褐', '褒', '襟', '襲', '西', '要', '覆', '覇', '見', '規', '視', '覚', '覧', '親', '観', '覺', '觀', '角', '解', '触', '言', '訂', '訃', '計', '訊', '討', '訓', '託', '記', '訟', '訣', '訪', '設', '許', '訳', '訴', '診', '註', '証', '詐', '詔', '評', '詞', '詠', '詣', '試', '詩', '詫', '詮', '詰', '話', '該', '詳', '誇', '誉', '誌', '認', '誓', '誕', '誘', '語', '誠', '誤', '誦', '説', '読', '誰', '課', '誹', '調', '談', '請', '諏', '諒', '論', '諦', '諧', '諭', '諮', '諷', '諸', '諺', '諾', '謀', '謁', '謂', '謄', '謎', '謙', '講', '謝', '謡', '謬', '謹', '證', '識', '譜', '警', '譬', '譯', '議', '譲', '護', '讀', '變', '谷', '豆', '豊', '豚', '象', '豪', '豹', '貌', '貝', '貞', '負', '財', '貢', '貧', '貨', '販', '貪', '貫', '責', '貯', '貰', '貴', '買', '貸', '費', '貼', '貿', '賀', '賂', '賃', '賄', '資', '賊', '賓', '賛', '賜', '賞', '賠', '賢', '賣', '賤', '賦', '質', '賭', '購', '贈', '赤', '赦', '走', '赳', '赴', '起', '超', '越', '趣', '足', '距', '跡', '路', '跳', '践', '踊', '踏', '踪', '蹟', '蹴', '躍', '身', '車', '軌', '軍', '軒', '軟', '転', '軸', '軽', '較', '載', '輔', '輕', '輝', '輩', '輪', '輯', '輸', '輿', '轄', '轉', '轟', '辛', '辞', '辣', '辰', '辱', '農', '辺', '辻', '込', '迂', '迄', '迅', '迎', '近', '返', '迦', '迫', '迭', '述', '迷', '追', '退', '送', '逃', '逆', '透', '逐', '逓', '途', '逗', '這', '通', '逝', '逞', '速', '造', '逢', '連', '逮', '週', '進', '逸', '遂', '遅', '遇', '遊', '運', '遍', '過', '道', '達', '違', '遙', '遜', '遠', '遡', '遣', '遥', '適', '遭', '遮', '遵', '遷', '選', '遺', '遼', '避', '邁', '還', '邑', '那', '邦', '邪', '邸', '郁', '郊', '郎', '郡', '部', '郭', '郵', '郷', '都', '鄙', '鄭', '酉', '酌', '配', '酎', '酒', '酔', '酢', '酪', '酬', '酵', '酷', '酸', '醍', '醒', '醜', '醸', '采', '釈', '里', '重', '野', '量', '金', '釘', '釜', '針', '釣', '鈍', '鈴', '鉄', '鉛', '鉢', '鉦', '鉱', '鉾', '銀', '銃', '銅', '銑', '銘', '銚', '銭', '鋏', '鋒', '鋤', '鋭', '鋳', '鋸', '鋼', '錘', '錠', '錦', '錫', '錬', '錮', '錯', '録', '鍋', '鍛', '鍬', '鍵', '鍾', '鎌', '鎖', '鎚', '鎮', '鏡', '鐘', '鐵', '鑑', '鑓', '長', '門', '閉', '開', '閑', '間', '関', '閣', '閥', '閲', '闇', '闊', '闘', '關', '阜', '阪', '防', '阻', '阿', '陀', '附', '降', '限', '陛', '院', '陣', '除', '陥', '陪', '陰', '陳', '陵', '陶', '陸', '険', '陽', '隅', '隆', '隈', '隊', '階', '随', '隔', '隙', '際', '障', '隠', '隣', '隨', '隱', '隷', '隻', '隼', '雀', '雄', '雅', '集', '雇', '雉', '雌', '雑', '雛', '雜', '離', '難', '雨', '雪', '雫', '雰', '雲', '零', '雷', '電', '需', '震', '霊', '霜', '霞', '霧', '露', '靈', '青', '靖', '静', '靜', '非', '面', '革', '靴', '鞍', '鞘', '鞠', '鞭', '韓', '韮', '音', '韻', '響', '頁', '頂', '頃', '項', '順', '須', '預', '頑', '頒', '頓', '領', '頭', '頰', '頸', '頻', '頼', '題', '額', '顎', '顔', '顕', '願', '顛', '類', '顧', '風', '颯', '飛', '食', '飢', '飯', '飲', '飼', '飽', '飾', '餅', '養', '餌', '餓', '館', '饒', '饗', '首', '香', '馨', '馬', '馭', '馴', '駄', '駅', '駆', '駈', '駐', '駒', '駿', '騎', '騒', '験', '騙', '騰', '驚', '驢', '骨', '骸', '髄', '體', '高', '髪', '髭', '鬚', '鬱', '鬼', '魁', '魂', '魅', '魔', '魚', '鮎', '鮒', '鮫', '鮭', '鮮', '鯉', '鯖', '鯛', '鯨', '鳥', '鳩', '鳳', '鳴', '鳶', '鴎', '鴨', '鴻', '鵜', '鵡', '鵬', '鶏', '鶴', '鷲', '鷹', '鷺', '鸚', '鹿', '麓', '麗', '麟', '麦', '麹', '麺', '麻', '麿', '黄', '黎', '黒', '黙', '鼎', '鼓', '鼠', '鼻', '齢', '𠮟']
>>>