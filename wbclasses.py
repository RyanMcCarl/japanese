#!/usr/env/python3
#
# -*- coding: utf-8 -*-
# wbclasses
#

from functools import lru_cache
from wbutilities import write_files, write_dict, write_json, write_csv, sort_csv, \
dict_values_to_list, get_csv, read_json, get_integer_value_stats, \
get_number_of_integers, list_of_dicts_to_dict
from readingjp import *
from ast import literal_eval
from wbclasses import *
from pymongo import MongoClient
from os.path import expanduser

class Character(object):
    """Use the character as the variable name and pass a string representation of the character as the first argument.

        Example: `梶 = Kanji("梶")`

        Note that you should instantiate each character as a Kanji or Kana object, not a "Character" object.

        """

    def __init__(self, char):
        self.char = char

    def __str__(self):
        return str(self.char)
    
    def __repr__(self):
        return str(self.char)

    def get_char(self):
        return str(self.char)

class Kanji(Character):
    """Use the character as the variable name and pass a string representation of the character as the first argument.
    Note that you should instantiate each character as a Kanji or Kana object, not a 'Character' object.
"""

    def __init__(self, char, aozora="", blogs=None, components=[], count=None, 
        edict_common=None, freq=None, gsf=None, heisig=None, henshall=None, jinmeiyo=None,
        joyo=None, kanjidic=None, kklc=None, kunyomi=[], kyoiku=None, mainichi=None,
        meaning=[], median=None, novels=None, onyomi=[], pattern="",
        radicals=[], related_kanji=[],  rm=None, rtktwo=None, sentences=[],
        stroke_count=None, tags=[], twitter=None, variety=None, wikipedia=None, 
        yatskov_novels=None):

        Character.__init__(self, char)
        self.aozora = self.get_aozora()
        self.bigrams = self.get_bigrams()
        self.blogs = self.get_blogs()
        self.components = self.get_components()
        self.edict_common = self.get_edict_common()
        self.sentences = self.get_sentences()
        self.gsf = self.get_gsf()
        self.heisig = self.get_heisig()
        self.henshall = self.get_henshall()
        self.jinmeiyo = self.get_jinmeiyo()
        self.joyo = self.get_joyo()
        self.kanjidic = self.get_kanjidic()
        self.kklc = self.get_kklc()
        #self.kunyomi = self.get_kunyomi()
        self.kyoiku = self.get_kyoiku()
        self.mainichi = self.get_mainichi()
        self.meaning = self.get_meaning()
        self.novels = self.get_novels()
        #self.onyomi = self.get_onyomi()
        self.pattern = self.get_pattern()
        self.radicals = self.get_radicals()
        self.related_kanji = self.get_related_kanji()
        self.rm = self.get_rm()
        self.rtktwo = self.get_rtktwo()
        self.stroke_count = self.get_stroke_count()
        self.tags = []
        self.twitter = self.get_twitter()
        self.variety = self.get_variety()
        self.wikipedia = self.get_wikipedia()
        self.yatskov_novels = self.get_yatskov_novels()

        self.count = self.get_count()
        self.mean = self.get_mean()
        self.median = self.get_median()
        self.attributes = self.get_attribute_dict()
        self.get_data()


    @staticmethod
    def get_coll(db='jp', coll='kanji'):
        client = MongoClient()
        return client.db.coll

    def get_attribute_dict(self):
        return str([str(str(attr) + ': ' + str(value)) for attr, value in vars(self).items()])

    def write_csv(self):
        kanji_list = [Kanji(l) for l in self.get_legitimate_kanji()]
        with open('output/usefulkanji.csv', mode='w') as outfile:
            for char in kanji_list:
                line = str('\t'.join([char, char.mean, 
                    ''.join(char.related_kanji),
                    ''.join(char.bigrams),
                 ''.join(char.onyomi),
                 ''.join(char.kunyomi),
                 ''.join(char.radicals),
                 ''.join(char.components),
                 ''.join(char.meanings),
                 char.pattern,
                 char.heisig,
                 char.kklc,
                 '\n']))
                outfile.writelines(line)
        return("Wrote CSV file to output/usefulkanji.csv")


    def update_mongo(self):
        client = MongoClient('mongodb://localhost:27017/')
        db = client.jp
        coll = db.kanji
        adict = {"$set": {attr: value for attr, value in vars(self).items()}}
        print(str(adict))
        print(type(adict))
        coll.update({"char": self.char}, adict, upsert=True)
        #cursor = coll.find_one({"char": self.char}, {"_id:": 0, "attributes": 0})
        return "Updated."

    def get_legitimate_kanji(self):
        with open('Japanese/kanji/data/mixed/rm_2323_kanji.txt', mode='r', encoding='utf-8') as infile:
            legitimate_kanji = {k.strip() for k in infile.readlines()}
            return legitimate_kanji

    def get_aozora(self):
        with open("Japanese/kanji/data/frequency/aozora_kanji_freq.txt", mode="r", encoding="utf-8") as infile:
            thelist = [l.strip() for l in infile.readlines()]
            if self.char in set(thelist):
                for i, v in enumerate(thelist):
                    if self.char == v.strip():
                        char_num = i + 1
                        return char_num
                        break

    def get_bigrams(self):
        legitimate_kanji = self.get_legitimate_kanji()
        with open("Japanese/kanji/data/mappings/kanji_bigrams.csv", mode="r", encoding="utf-8") as infile:
            thelist = [l.strip() for l in infile.readlines()]
            for line in thelist:
                line = line.split('\t')
                if line[0] == self.char:
                    if len(line) > 1:
                        return list({l for l in line[1].strip() if l in legitimate_kanji})
                    else:
                        return []
                    break


    def get_blogs(self):
        with open("Japanese/kanji/data/frequency/blog_kanji_by_wordfreq.txt", mode="r", encoding="utf-8") as infile:
            thelist = [l.strip() for l in infile.readlines()]
            if self.char in set(thelist):
                for i, v in enumerate(thelist):
                    list_char = v.strip()
                    if self.char == v.strip():
                        char_num = i + 1
                        return char_num
                        break


    def get_components(self):
        legitimate_kanji = self.get_legitimate_kanji()
        with open('Japanese/kanji/data/mappings/components_by_kanji.csv') as infile:
            components_by_kanji = (l.strip().split('\t') for l in infile.readlines())
            for i in range(len(list(components_by_kanji)) - 1):
                try:
                    aline = next(components_by_kanji)
                    line = aline.split('\t')
                    kanji = line[0]
                    if kanji == self.char:
                        if len(line) > 1:
                            return list({l for l in line[1].strip() if l in legitimate_kanji})
                        else:
                            return []
                        break
                except:
                    return []


    def get_count(self):
        return None


    def get_heisig(self):
        with open("Japanese/kanji/data/pedagogical/heisig_kanji.txt", mode="r", encoding="utf-8") as infile:
            thelist = [l.strip() for l in infile.readlines()]
            if self.char in set(thelist):
                for i, v in enumerate(thelist):
                    if self.char == v.strip():
                        char_num = i + 1
                        return char_num
                        break


    def get_gsf(self):
        with open("Japanese/kanji/data/mixed/con_kolivas_gsf_list.txt", mode="r", encoding="utf-8") as infile:
            thelist = [l.strip() for l in infile.readlines()]
            if self.char in set(thelist):
                for i, v in enumerate(thelist):
                    list_char = v.strip()
                    if self.char == v.strip():
                        char_num = i + 1
                        return char_num
                        break


    def get_edict_common(self):
        with open("Japanese/kanji/data/frequency/kanji_in_edict_common_unsorted.txt", mode="r", encoding="utf-8") as infile:
            thelist = [l.strip() for l in infile.readlines()]
            if self.char in set(thelist):
                return True


    def get_henshall(self):
        with open("Japanese/kanji/data/pedagogical/henshall_kanji.txt", mode="r", encoding="utf-8") as infile:
            thelist = [l.strip() for l in infile.readlines()]
            if self.char in set(thelist):
                for i, v in enumerate(thelist):
                    list_char = v.strip()
                    if self.char == v.strip():
                        char_num = i + 1
                        return char_num
                        break


    def get_jinmeiyo(self):
        with open("Japanese/kanji/data/traditional/jinmeiyo_kanji.txt", mode="r", encoding="utf-8") as infile:
            thelist = [l.strip() for l in infile.readlines()]
            if self.char in set(thelist):
                for i, v in enumerate(thelist):
                    list_char = v.strip()
                    if self.char == v.strip():
                        char_num = i + 1
                        return char_num + 2137 # Accounting for the kyoiku and joyo kanji
                        break


    def get_jlpt(self):
        with open("Japanese/kanji/data/traditional/jlpt_kanji.txt", mode="r", encoding="utf-8") as infile:
            thelist = [l.strip() for l in infile.readlines()]
            if self.char in set(thelist):
                for i, v in enumerate(thelist):
                    list_char = v.strip()
                    if self.char == v.strip():
                        char_num = i + 1
                        return char_num
                        break


    def get_joyo(self):
        with open("Japanese/kanji/data/traditional/joyo_non_kyoiku_kanji.txt", mode="r", encoding="utf-8") as infile:
            thelist = [l.strip() for l in infile.readlines()]
            if self.char in set(thelist):
                for i, v in enumerate(thelist):
                    list_char = v.strip()
                    if self.char == v.strip():
                        char_num = i + 1
                        return char_num + 1006 # Accounting for the kyoiku kanji
                        break


    def get_kanjidic(self):
        with open("Japanese/kanji/data/frequency/kanjidic_freq.txt", mode="r", encoding="utf-8") as infile:
            thelist = [l.strip() for l in infile.readlines()]
            if self.char in set(thelist):
                for i, v in enumerate(thelist):
                    list_char = v.strip()
                    if self.char == v.strip():
                        char_num = i + 1
                        return char_num
                        break


    def get_kic(self):
        with open("Japanese/kanji/data/pedagogical/kanji_in_context_kanji.txt", mode="r", encoding="utf-8") as infile:
            thelist = [l.strip() for l in infile.readlines()]
            if self.char in set(thelist):
                for i, v in enumerate(thelist):
                    list_char = v.strip()
                    if self.char == v.strip():
                        char_num = i + 1
                        return char_num
                        break



    def get_kklc(self):
        with open("Japanese/kanji/data/pedagogical/kklc_kanji.txt", mode="r", encoding="utf-8") as infile:
            thelist = [l.strip() for l in infile.readlines()]
            if self.char in set(thelist):
                for i, v in enumerate(thelist):
                    list_char = v.strip()
                    if self.char == v.strip():
                        char_num = i + 1
                        return char_num
                        break


    def get_kunyomi(self):
        return []


    def get_kyoiku(self):
        with open("Japanese/kanji/data/traditional/kyoiku_kanji.txt", mode="r", encoding="utf-8") as infile:
            thelist = [l.strip() for l in infile.readlines()]
            if self.char in set(thelist):
                for i, v in enumerate(thelist):
                    list_char = v.strip()
                    if self.char == v.strip():
                        char_num = i + 1
                        return char_num
                        break


    def get_mainichi(self):
        with open("Japanese/kanji/data/frequency/mainichi_kanji_by_wordfreq.txt", mode="r", encoding="utf-8") as infile:
            thelist = [l.strip() for l in infile.readlines()]
            if self.char in set(thelist):
                for i, v in enumerate(thelist):
                    list_char = v.strip()
                    if self.char == v.strip():
                        char_num = i + 1
                        return char_num
                        break


    def get_mean(self):
        return None


    def get_meaning(self):
        try:
            meaning = db.kanji.find({"name": self.char}, {"meaning": 1, "_id": 0})
            self.meaning  = meaning
            return(str(meaning))
        except:
            return []


    def get_median(self):
        return None


    def get_news(self):
        with open("Japanese/kanji/data/frequency/kanji_freq_news.txt", mode="r", encoding="utf-8") as infile:
            thelist = [l.strip() for l in infile.readlines()]
            if self.char in set(thelist):
                for i, v in enumerate(thelist):
                    list_char = v.strip()
                    if self.char == v.strip():
                        char_num = i + 1
                        return char_num
                        break


    def get_novels(self):
        with open("Japanese/kanji/data/frequency/kanji_freq_novels.txt", mode="r", encoding="utf-8") as infile:
            thelist = [l.strip() for l in infile.readlines()]
            if self.char in set(thelist):
                for i, v in enumerate(thelist):
                    list_char = v.strip()
                    if self.char == v.strip():
                        char_num = i + 1
                        return char_num
                        break


    def get_pattern(self):
        with open('Japanese/kanji/data/mappings/patterns_by_kanji.csv') as infile:
            patterns_by_kanji = (l.strip().split('\t') for l in infile.readlines())
            for i in range(len(list(patterns_by_kanji)) - 1):
                try:
                    aline = next(patterns_by_kanji)
                    line = aline.split('\t')
                    kanji = line[0]
                    if kanji == self.char:
                        if len(line) > 1:
                            return line[1]
                        else:
                            return []
                        break
                except:
                    return []


    def get_radicals(self):
        legitimate_kanji = self.get_legitimate_kanji()
        with open('Japanese/kanji/data/mappings/radicals_by_kanji.csv') as infile:
            radicals_by_kanji = (l.strip().split('\t') for l in infile.readlines())
            for i in range(len(list(radicals_by_kanji)) - 1):
                try:
                    aline = next(radicals_by_kanji)
                    line = aline.split('\t')
                    kanji = line[0]
                    if kanji == self.char:
                        if len(line) > 1:
                            return list({l for l in line[1].strip() if l in legitimate_kanji})
                        else:
                            return []
                        break
                except:
                    return []


    def get_related_kanji(self):
        legitimate_kanji = self.get_legitimate_kanji()
        with open("Japanese/kanji/data/mappings/related_kanji.csv", mode="r", encoding="utf-8") as infile:
            thelist = [l.strip() for l in infile.readlines()]
            for line in thelist:
                line = line.split('\t')
                if line[0] == self.char:
                    if len(line) > 1:
                        return list({l for l in line[1].strip() if l in legitimate_kanji})
                    else:
                        return []
                    break


    def get_rm(self):
        with open("Japanese/kanji/data/mixed/rm_kanji_rank_grouped.txt", mode="r", encoding="utf-8") as infile:
            thelist = [l.strip() for l in infile.readlines()]
            if self.char in set(thelist):
                for i, v in enumerate(thelist):
                    list_char = v.strip()
                    if self.char == v.strip():
                        char_num = i + 1
                        return char_num
                        break


    def get_rtktwo(self):
        with open("Japanese/kanji/data/pedagogical/rtk_2_example_order.txt", mode="r", encoding="utf-8") as infile:
            thelist = [l.strip() for l in infile.readlines()]
            if self.char in set(thelist):
                for i, v in enumerate(thelist):
                    list_char = v.strip()
                    if self.char == v.strip():
                        char_num = i + 1
                        return char_num
                        break


    def get_sentences(self):
        return []


    def get_stroke_count(self):
        return []


    def get_twitter(self):
        with open("Japanese/kanji/data/frequency/twitter_kanji_frequency.txt", mode="r", encoding="utf-8") as infile:
            thelist = [l.strip() for l in infile.readlines()]
            if self.char in set(thelist):
                for i, v in enumerate(thelist):
                    list_char = v.strip()
                    if self.char == v.strip():
                        char_num = i + 1
                        return char_num
                        break


    def get_variety(self):
        with open("Japanese/kanji/data/frequency/kanji_freq_variety_sources.txt", mode="r", encoding="utf-8") as infile:
            thelist = [l.strip() for l in infile.readlines()]
            if self.char in set(thelist):
                for i, v in enumerate(thelist):
                    list_char = v.strip()
                    if self.char == v.strip():
                        char_num = i + 1
                        return char_num
                        break


    def get_wikipedia(self):
        with open("Japanese/kanji/data/frequency/yatskov_wikipedia_kanji.txt", mode="r", encoding="utf-8") as infile:
            thelist = [l.strip() for l in infile.readlines()]
            if self.char in set(thelist):
                for i, v in enumerate(thelist):
                    list_char = v.strip()
                    if self.char == v.strip():
                        char_num = i + 1
                        return char_num
                        break




    def get_yatskov_novels(self):
        with open("Japanese/kanji/data/frequency/yatskov_novels_kanji.txt", mode="r", encoding="utf-8") as infile:
            thelist = [l.strip() for l in infile.readlines()]
            if self.char in set(thelist):
                for i, v in enumerate(thelist):
                    list_char = v.strip()
                    if self.char == v.strip():
                        char_num = i + 1
                        return char_num
                        break


    def get_data(self):
        kdic2 = read_json("Japanese/kanji/archive/kanjidic2.json")
        for i in range(len(kdic2)):
            row = kdic2[i]
            if row["literal"] == self.char:
                entry = {"char": self.char}
                entry = add_readings(row, entry)
                entry = add_meanings(row, entry)
                entry = get_freq_tags(row, entry)
                entry = get_jlpt_tags(row, entry)
                entry = get_grade_tags(row, entry)
                entry = get_strokecount_tags(row, entry)
                entry = get_heisig_tags(row, entry)
                entry = get_kic_tags(row, entry)
                entry = get_kklc_tags(row, entry)
                entry = get_rmfreq_tags(row, entry)

                try:
                    self.tags = [l for l in entry["tags"]]
                except:
                    pass
                try:
                    self.onyomi = [o for o in entry["readings"]["onyomi"]]
                except:
                    pass
                try:
                    self.kunyomi = [k for k in entry["readings"]["kunyomi"]]
                except:
                    pass
                try:
                    self.tags = [t for t in entry["tags"]]
                except:
                    pass
                try:
                    self.meanings = [m for m in entry["meanings"]]
                except:
                    pass

class Kana(Character):
    def __init__(self, char, reading="", freq=None):
        """
Use the character as the variable name and pass a string representation of the character as the first argument.

        Example: `梶 = Kanji("梶")`

Note that you should instantiate each character as a Kanji or Kana object, not a "Character" object.

        """
        Character.__init__(self, char)
        self.char = char
        self.reading = reading
        self.freq = freq


class Word(object):

    def __init__(self, word, reading="", meaning=[], pos=[],\
     freq={}, misc=[], field="", edict_common = None):
        """
Use the word as the variable name and pass a string representation of the word as the first argument.

        Example: 梶 = Word("梶")
        """
        self.word = word
        self.reading = reading
        self.meaning = meaning
        self.pos = pos
        self.freq = freq
        self.misc = misc
        self.field = field
        self.edict_common = edict_common

    @staticmethod
    def get_word_dict(filepath='Japanese/words/archive/jp_words.dict'):
    """
    Example of return value:
      >>> word_dict['亜']
      {'reading': 'あ', 'meaning': ['sub-', '-ous (indicating a low oxidation state)', ' -ite'],
          'word': '亜', 'pos': 'pref'}

    """
    with open(filepath, mode='r') as infile:
        return literal_eval(infile.read())

    @staticmethod
    def get_coll(db='jp', coll='kanji'):
        client = MongoClient()
        return client.db.coll




        def get_reading(word_dict, coll=get_coll('jp', 'words')):
            for k in word_dict.keys():
                filt = {'word': k}
                upd = {'$set': {'reading': word_dict[k]['reading']}}
                coll.update(filt, upd)
                return "Added reading"


def add_pos(word_dict, coll=get_coll('jp', 'words')):
    for k in word_dict.keys():
        filt = {'word': k}
        upd = {'$set': {'pos': word_dict[k]['pos']}}
        coll.update(filt, upd)
    return "Added POS"

def add_meaning(word_dict, coll=get_coll('jp', 'words')):
    for k in word_dict.keys():
        filt = {'word': k}
        upd = {'$set': {'meaning': word_dict[k]['meaning']}}
        coll.update(filt, upd)
    return "Added meaning"


# Instantiate a kana object "ひ"

ひ = Kana("ひ")
print(ひ.char)

# Instantiate a Word object
梶 = Word("梶")

print(梶.word)

# Instantiate a kanji object "仮"
仮 = Kanji("仮")
print(仮.char)
