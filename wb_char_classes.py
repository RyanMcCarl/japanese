#!/usr/env/python3
#
# -*- coding: utf-8 -*-
# wb_char_classes
#

from kanji_lists import *
from functools import lru_cache
from wbutilities import connect_mongo, update_mongo, write_dict, write_json, write_csv, sort_csv, \
dict_values_to_list, get_csv, read_json, get_integer_value_stats, \
get_number_of_integers, list_of_dicts_to_dict
from pymongo import MongoClient

class Character(object):
    """Use the character as the variable name and pass a string representation of the character as the first argument.

        Example: `梶 = Kanji("梶")`

        Note that you should instantiate each character as a Kanji or Kana object, not a "Character" object.

        """
    def __init__(self, char):
        self.char = char.strip()


    def __str__(self):
        return str(self.char).strip()


    def __repr__(self):
        return str(self.char).strip()


    def get_char(self):
        return str(self.char).strip()


    @staticmethod
    def make_gen(enumerable):
        copy = enumerable
        return (e for e in copy)


class Kanji(Character):
    """Use the character as the variable name and pass a string representation of the character as the first argument.
    Note that you should instantiate each character as a Kanji or Kana object, not a 'Character' object.
"""

    @staticmethod
    def get_lists():
        kanji_list_dict = {}
        for i in range(len(ORDERED_KANJI_LISTS)):
            with open(ORDERED_KANJI_LISTS[i]['list_path'], mode='r', encoding='utf-8') as infile:
                kanji_list_dict[ORDERED_KANJI_LISTS[i]['list_name']] = enumerate([l.strip() for l in infile.readlines()], start=1)                
        for i in range(len(KANJI_CSVS)):
            with open(KANJI_CSVS[i]['csv_path'], mode='r', encoding='utf-8') as infile:
                kanji_list_dict[KANJI_CSVS[i]['csv_name']] = ([l.strip().split('\t') for l in infile.readlines()])
        for i in range(len(UNORDERED_KANJI_LISTS)):
            with open(UNORDERED_KANJI_LISTS[i]['set_path'], mode='r', encoding='utf-8') as infile:
                kanji_list_dict[UNORDERED_KANJI_LISTS[i]['set_name']] = (l.strip() for l in infile.readlines())
        return kanji_list_dict


    def __init__(self, char):

        Character.__init__(self, char)
        self.bigrams = self.get_value('bigrams')
        self.blogs = self.get_value('blogs')
        self.components = self.get_value('components')
        self.edict_common = self.get_value('edict_common')
        self.gsf = self.get_value('gsf')
        self.heisig = self.get_value('heisig')
        self.henshall = self.get_value('henshall')
        self.jinmeiyo = self.get_value('jinmeiyo')
        self.joyo = self.get_value('joyo')
        self.kanjidic = self.get_value('kanjidic')
        self.kklc = self.get_value('kklc')
        self.kunyomi = self.get_value('kunyomi')
        self.kyoiku = self.get_value('kyoiku')
        self.mainichi = self.get_value('mainichi')
        #self.meaning = self.get_value('meaning')
        self.novels = self.get_value('novels')
        #self.onyomi = self.get_value('onyomi')
        self.pattern = self.get_value('pattern')
        self.radical_list = self.get_value('radical_list')
        self.related = self.get_value('related_kanji')
        self.rm_rank = self.get_value('rm_rank')
        self.rm2323 = self.get_value('rm2323')
        self.rtk_two = self.get_value('rtktwo')
        #self.sentences = self.get_value('sentences')
        #self.stroke_count = self.get_value('stroke_count')
        #self.tags = []
        self.twitter = self.get_value('twitter')
        self.variety = self.get_value('variety')
        self.wikipedia = self.get_value('wikipedia')
        self.yatskov_novels = self.get_value('yatskov_novels')


    @lru_cache(maxsize=10)
    def get_value(self, attrib):
        for k, v in Kanji.get_lists().items():
            if k == attrib:
                newgen = Kanji.make_gen(v)  #Ex: (0, '日')
                for i in newgen:
                    atuple = i
                    if attrib in {'edict_common', 'rm2323'}:
                        return True
                    if self.char in atuple:
                        if attrib == 'joyo':
                            return atuple[0] + 1006
                        if attrib == 'jinmeiyo':
                            return atuple[0] + 2137
                        return atuple[0]
                    if attrib == 'pattern':
                        if self.char in atuple[0]:
                            return atuple[1]
                    if attrib in {'bigrams', 'components', 'radicals', 'related'}:
                        if self.char in atuple[0]:
                            return [c for c in atuple[1]]

    @staticmethod
    def get_kanji_dict():
        """
        Example of return value:
        >>> kanji_dict['亜']
            {'codepoints': [{'cp_type': 'ucs', 'cp_value': '4e9c'}, {'cp_type': 'jis208', 'cp_value': '16-01'}], 
            'stroke_count': 7, 'variant': {'var_type': 'jis208', 'variant': '48-19'}, 
            'radicals': [{'rad_type': 'classical', 'rad_value': 7}, {'rad_type': 'nelson_c', 'rad_value': 1}], 
            'literal': '亜', 'readings': [{'r_type': 'pinyin', 'reading': 'ya4'}, {'r_type': 'korean_r', 'reading': 'a'}, 
            {'r_type': 'korean_h', 'reading': '아'}, {'r_type': 'ja_on', 'reading': 'ア'}, 
            {'r_type': 'ja_kun', 'reading': 'つ.ぐ'}], 'grade': 8, 
            'query_codes': [{'qc_type': 'skip', 'q_code': '4-7-1'}, {'qc_type': 'sh_desc', 'q_code': '0a7.14'}, 
            {'qc_type': 'four_corner', 'q_code': '1010.6'}, {'qc_type': 'deroo', 'q_code': '3273'}], 
            'freq': 1509, 
            'jlpt': 1, 
            'meanings': [{'meaning': 'Asia'}, {'meaning': 'rank next'}, {'meaning': 'come after'}, 
            {'meaning': '-ous'}, {'m_lang': 'fr', 'meaning': 'Asie'}, {'m_lang': 'fr', 'meaning': 'suivant'}, 
            {'m_lang': 'fr', 'meaning': 'sub-'}, {'m_lang': 'fr', 'meaning': 'sous-'}, 
            {'m_lang': 'es', 'meaning': 'pref. para indicar'}, {'m_lang': 'es', 'meaning': 'venir después de'}, 
            'm_lang': 'es', 'meaning': 'Asia'}, {'m_lang': 'pt', 'meaning': 'Ásia'}, {'m_lang': 'pt', 'meaning': 'próxima'}, 
            {'m_lang': 'pt', 'meaning': 'o que vem depois'}, {'m_lang': 'pt', 'meaning': '-ous'}], 
            'dic_numbers': [{'dic_ref': '43', 'dr_type': 'nelson_c'}, {'dic_ref': '81', 'dr_type': 'nelson_n'}, 
            {'dic_ref': '3540', 'dr_type': 'halpern_njecd'}, {'dic_ref': '2204', 'dr_type': 'halpern_kkld'}, 
            {'dic_ref': '1809', 'dr_type': 'heisig'}, {'dic_ref': '1331', 'dr_type': 'gakken'}, 
            {'dic_ref': '525', 'dr_type': 'oneill_names'}, {'dic_ref': '1788', 'dr_type': 'oneill_kk'}, 
            {'dic_ref': '272', 'dr_type': 'moro'}, {'dic_ref': '997', 'dr_type': 'henshall'}, 
            {'dic_ref': '1616', 'dr_type': 'sh_kk'}, {'dic_ref': '1032', 'dr_type': 'jf_cards'}, 
            {'dic_ref': '1092', 'dr_type': 'tutt_cards'}, {'dic_ref': '1818', 'dr_type': 'kanji_in_context'}, 
            {'dic_ref': '35', 'dr_type': 'kodansha_compact'}, {'dic_ref': '1827', 'dr_type': 'maniette'}]}

        """
        kanji_dict_list = get_list_from_json_file(json_file_path="Japanese/kanji/archive/kanjidic2.json")
        return {kanji_dict_list[i]['literal']: kanji_dict_list[i] for i in range(len(kanji_dict_list))}



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


def main():
    with open('Japanese/kanji/data/mixed/rm_2323_kanji.txt', mode='r') as infile:
        kgen = (Kanji(k) for k in infile.readlines())
    #testkanji = [Kanji(k) for k in ['中', '一', '大','上','本']]
    for kanji in kgen:
        for k, v in kanji.__dict__.items():
            update_mongo(filter_key='literal', filter_value=str(kanji).strip(), var_name=k,\
                var_value=v, db='jp', coll='kanji')

if __name__ == '__main__':
    main()
