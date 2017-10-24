#!/usr/env/python3
#
# -*- coding: utf-8 -*-
# readingjp.py
#
from wbutilities import write_files, write_dict, write_json, write_csv, sort_csv, \
dict_values_to_list, get_csv, read_json, get_integer_value_stats, \
get_number_of_integers, list_of_dicts_to_dict
from wbclasses import *
from pymongo import MongoClient
from os.path import expanduser

def get_data(kanji_dict={}):
    kanjidic2 = json.loads("Japanese/kanji/archive/kanjidic2.json")
    # For testing:
    print(type(kanjidic2))
    print(len(kanjidic2))
    return kanjidic2

def parse_kanjidic2(kdic2=get_data(), kanji_dict={}):
    for i in range(len(kdic2)):
        row = kdic2[i]
        char = row["literal"]
        entry = {"char": char}
        # char field
        kanji_dict[char] = {}
        kanji_dict[char]["char"] = char
        # readings field

        entry = add_readings(row, entry)

        # meanings field

        entry = add_meanings(row, entry)

        # tags field
        # freq, grade, jlpt, and stroke_count fields
        entry = get_freq_tags(row, entry)
        entry = get_jlpt_tags(row, entry)
        entry = get_grade_tags(row, entry)
        entry = get_strokecount_tags(row, entry)
        entry = get_heisig_tags(row, entry)
        entry = get_kic_tags(row, entry)
        entry = get_kklc_tags(row, entry)
        entry = get_rmfreq_tags(row, entry)

        # radicals field

        entry = add_radicals(row, entry)

        # dict_numbers field

        entry = add_dict_numbers(row, entry)

        # variants field

        entry = add_variants(row, entry)

        kanji_dict["char"] = entry

    return kanji_dict

def get_freq_tags(row, entry, tags=set()):
    for item in row.keys():
        if 'freq' in item:
            freq = row['freq']
            entry["kanjidic"] = freq
            if freq <= 100:
                tags.add("100")
            elif freq <= 500:
                tags.add("500")
            elif freq <= 1000:
                tags.add("1000")
            elif freq <= 1500:
                tags.add("1500")
            elif freq <= 2000:
                tags.add("2000")
            elif freq <= 2500:
                tags.add("2500")
            elif freq <= 3000:
                tags.add("3000")
    try:
        if entry["tags"] and tags:
            entry["tags"] = tags | entry["tags"]
        elif entry["tags"] and not tags:
            pass
        elif tags and not entry["tags"]:
            entry["tags"] = tags
    except KeyError:
        pass

    return entry

def get_grade_tags(row, entry, tags=set()):
    for item in row.keys():
        if 'grade' in item:
            grade = row['grade']
            entry["grade"] = grade
            if grade <= 6:
                tags.add("Grade " + str(grade))
                tags.add("kyoiku")
                tags.add("joyo")
            if grade == 8:
                tags.add("joyo")
            if grade == 9:
                tags.add("jinmeiyou")
    try:
        if entry["tags"]:
            entry["tags"] = tags | entry["tags"]
        else:
            entry["tags"] = tags
    except KeyError:
        entry["tags"] = tags
    return entry

def get_jlpt_tags(row, entry, tags=set()):
    for item in row.keys():
        if 'jlpt' in item:
            jlpt = row['jlpt']
            entry["jlpt"] = jlpt
            tags.add("JLPT " + str(jlpt))

    try:
        if entry["tags"]:
            entry["tags"] = tags | entry["tags"]
        else:
            entry["tags"] = tags
    except KeyError:
        entry["tags"] = tags
    return entry

def get_strokecount_tags(row, entry, tags=set()):
    for item in row.keys():
        if 'stroke_count' in item:
            stroke_count = row['stroke_count']
            entry["stroke_count"] = stroke_count
            if stroke_count <= 6:
                tags.add("simple")
            elif stroke_count >= 11:
                tags.add("complex")
    try:
        if entry["tags"]:
            entry["tags"] = tags | entry["tags"]
        else:
            entry["tags"] = tags
    except KeyError:
        entry["tags"] = tags
    return entry

def get_kic_tags(row, entry, tags=set()):
    # Kanji in context
    with open("Japanese/kanji/data/pedagogical/kanji_in_context_kanji.txt", mode="r", encoding="utf-8") as infile:
        thelist = infile.readlines()
        for i, v in enumerate(thelist):
            thelist[i] = thelist[i].strip()
            if v.strip() == entry["char"]:
                tags.add("kanji_in_context")
                if i <= 500:
                    tags.add("kic500")
                elif i <= 1000:
                    tags.add("kic1000")
                elif i <= 1500:
                    tags.add("kic1500")
                elif i <= 2000:
                    tags.add("kic2000")

    try:
        if entry["tags"]:
            entry["tags"] = tags | entry["tags"]
        else:
            entry["tags"] = tags
    except KeyError:
        entry["tags"] = tags
    return entry

def get_kklc_tags(row, entry, tags=set()):
    # Kodansha Kanji Learner's Course
    with open("Japanese/kanji/data/pedagogical/kklc_kanji.txt", mode="r", encoding="utf-8") as infile:
        thelist = infile.readlines()
        for i, v in enumerate(thelist):
            thelist[i] = thelist[i].strip()
            if v.strip() == entry["char"]:
                tags.add("kklc")
                if i <= 500:
                    tags.add("kklc500")
                elif i <= 1000:
                    tags.add("kklc1000")
                elif i <= 1500:
                    tags.add("kklc1500")
                elif i <= 2000:
                    tags.add("kklc2000")
    try:
        if entry["tags"]:
            entry["tags"] = tags | entry["tags"]
        else:
            entry["tags"] = tags
    except KeyError:
        entry["tags"] = tags
    return entry

def get_heisig_tags(row, entry, tags=set()):
                # Heisig, Remember the Kanji
    with open("Japanese/kanji/data/pedagogical/heisig_kanji.txt", mode="r", encoding="utf-8") as infile:
        thelist = infile.readlines()
        for i, v in enumerate(thelist):
            thelist[i] = thelist[i].strip()
            if v.strip() == entry["char"]:
                tags.add("heisig")
                if i <= 500:
                    tags.add("heisig500")
                elif i <= 1000:
                    tags.add("heisig1000")
                elif i <= 1500:
                    tags.add("heisig1500")
                elif i <= 2000:
                    tags.add("heisig2000")

    try:
        if entry["tags"]:
            entry["tags"] = tags | entry["tags"]
        else:
            entry["tags"] = tags
    except KeyError:
        entry["tags"] = tags
    return entry

def get_rmfreq_tags(row, entry, tags=set()):
                # By rm kanji scores list
    with open("Japanese/kanji/data/mixed/rm_kanji_rank_grouped.txt", mode="r", encoding="utf-8") as infile:
        thelist = infile.readlines()
        for i, v in enumerate(thelist):
            thelist[i] = thelist[i].strip()
            if v.strip() == entry["char"]:
                if i <= 500:
                    tags.add("rmjf500")
                elif i <= 1000:
                    tags.add("rmjf1000")
                elif i <= 1500:
                    tags.add("rmjf1500")
                elif i <= 2000:
                    tags.add("rmjf2000")
                elif i <= 2500:
                    tags.add("rmjf2500")
                elif i <= 3000:
                    tags.add("rmjf3000")
                elif i <= 3500:
                    tags.add("rmjf3500")

    try:
        if entry["tags"]:
            entry["tags"] = tags | entry["tags"]
        else:
            entry["tags"] = tags
    except KeyError:
        entry["tags"] = tags
    return entry

def add_radicals(row, entry, radicals=set(), rad_type="", rad_num=None):
    if "radicals" in row:
        for i in range(len(row["radicals"])):
            for k, v in row["radicals"][i].items():
                if "rad_type" in k:
                    rad_type = v
                elif "rad_value" in k:
                    rad_num = v
            radtup= tuple((rad_type, rad_num))
            radicals.add(radtup)
        entry["radicals"] = list(radicals)

    return entry

def add_meanings(row, entry, meanings=set()):
    assert isinstance(entry, dict)
    try:
        entry["meanings"] = {}
    except:
        print(entry)
    if "meanings" in row:
        for i in range(len(row["meanings"])):
            for k, v in row["meanings"][i].items():
                if not "m_lang" in row["meanings"][i].keys():
                    meanings.add(v)
        entry["meanings"] = list(meanings)

    return entry

def add_readings(row, entry, tags=set(), onyomi=set(), kunyomi=set(), pinyin=set()):
    if "readings" in row:
        entry["readings"] = {}
        for i in range(len(row["readings"])):
            if "ja_on" in row["readings"][i].values():
                for k, v in row["readings"][i].items():
                    if k == "reading":
                        onyomi.add(v)
            if "ja_kun" in row["readings"][i].values():
                for k, v in row["readings"][i].items():
                    if k == "reading":
                        kunyomi.add(v)
            if "pinyin" in row["readings"][i].values():
                for k, v in row["readings"][i].items():
                    if k == "reading":
                        pinyin.add(v)
        if pinyin:
            entry["pinyin"] = list(pinyin)
        if onyomi and kunyomi:
            entry["readings"] = {
                "onyomi": list(onyomi),
                "kunyomi": list(kunyomi)
            }
        elif onyomi:
            entry["readings"]["onyomi"] = list(onyomi)
            tags.add("onyomi only")
        else:
            entry["readings"]["kunyomi"] = list(kunyomi)
            tags.add("kunyomi only")

    try:
        if entry["tags"] and tags:
            entry["tags"] = tags | entry["tags"]
        elif entry["tags"] and not tags:
            pass
        elif tags and not entry["tags"]:
            entry["tags"] = tags
    except KeyError:
        pass
    return entry

def add_dict_numbers(row, entry, tags=set(), dic_numbers=set(), entry_num=None, dict_name=""):
    if "dic_numbers" in row:
        for i in range(len(row["dic_numbers"])):
            for k, v in row["dic_numbers"][i].items():
                if "dr_type" in k:
                    dict_name = v
                elif "dic_ref" in k:
                    entry_num = v
            dictup= tuple((dict_name, entry_num))
            dic_numbers.add(dictup)
            if "heisig" in dict_name:
                tags.add("heisig")
            if "henshall" in dict_name:
                tags.add("henshall")
            if "kanji_in_context" in dict_name:
                tags.add("kanji_in_context")
            if "halpern_kkld" in dict_name:
                tags.add("kkld")
        entry["dic_numbers"] = list(dic_numbers)

    try:
        if entry["tags"] and tags:
            entry["tags"] = tags | entry["tags"]
        elif entry["tags"] and not tags:
            pass
        elif tags and not entry["tags"]:
            entry["tags"] = tags
    except KeyError:
        pass
    return entry

def add_variants(row, entry, tags=set()):
    if "variant" in row:
        variants = set()
        var_type = ""
        var_num = int()
        for i in range(len(row["variant"].items())):
            for k, v in row["variant"].items():
                if "var_type" in k:
                    var_type = v
                elif "variant" in k:
                    var_num = v
            vartup= tuple((var_type, var_num))
            variants.add(vartup)
        entry["variants"] = list(variants)
        if variants:
            tags = tags.add("has_variant")
    try:
        if entry["tags"] and tags:
            entry["tags"] = tags | entry["tags"]
        elif entry["tags"] and not tags:
            pass
        elif tags and not entry["tags"]:
            entry["tags"] = tags
    except KeyError:
        pass
    return entry

def collect_kanji_tags(kanji_dict={}):
    # Kanji in context
    legitimate_kanji = set([k.strip() for k in infile.readlines()])
    kanjiset = set()
    kanji_files = [
        ('aozora', '/home/ryan/wbtools/Japanese/kanji/data/frequency/aozora_kanji_freq.txt'),
        ('blogs', '/home/ryan/wbtools/Japanese/kanji/data/frequency/blog_kanji_by_wordfreq.txt'),
        ('edict_common', '/home/ryan/wbtools/Japanese/kanji/data/frequency/kanji_in_edict_common_unsorted.txt'),
        ('gsf', '/home/ryan/wbtools/Japanese/kanji/data/mixed/con_kolivas_gsf_list.txt'),
        ('heisig', '/home/ryan/wbtools/Japanese/kanji/data/pedagogical/heisig_kanji.txt'),
        ('henshall', '/home/ryan/wbtools/Japanese/kanji/data/pedagogical/henshall_kanji.txt'),
        ('jinmeiyo', '/home/ryan/wbtools/Japanese/kanji/data/traditional/jinmeiyo_kanji.txt'),
        ('jlpt', '/home/ryan/wbtools/Japanese/kanji/data/traditional/jlpt_kanji.txt'),
        ('joyo', '/home/ryan/wbtools/Japanese/kanji/data/traditional/joyo_non_kyoiku_kanji.txt'),
        ('kanjidict', '/home/ryan/wbtools/Japanese/kanji/data/frequency/kanjidic_freq.txt'),
        ('kic', '/home/ryan/wbtools/Japanese/kanji/data/pedagogical/kanji_in_context_kanji.txt'),
        ('kklc', '/home/ryan/wbtools/Japanese/kanji/data/pedagogical/kklc_kanji.txt'),
        ('kyoiku', '/home/ryan/wbtools/Japanese/kanji/data/traditional/kyoiku_kanji.txt'),
        ('mainichi', '/home/ryan/wbtools/Japanese/kanji/data/frequency/mainichi_kanji_by_wordfreq.txt'),
        ('news', '/home/ryan/wbtools/Japanese/kanji/data/frequency/kanji_freq_news.txt'),
        ('novels', '/home/ryan/wbtools/Japanese/kanji/data/frequency/kanji_freq_novels.txt'),
        ('rm', '/home/ryan/wbtools/Japanese/kanji/data/mixed/rm_kanji_rank_grouped.txt'),
        ('rtktwo', '/home/ryan/wbtools/Japanese/kanji/data/pedagogical/rtk_2_example_order.txt'),
        ('twitter', '/home/ryan/wbtools/Japanese/kanji/data/frequency/twitter_kanji_frequency.txt'),
        ('variety', '/home/ryan/wbtools/Japanese/kanji/data/frequency/kanji_freq_variety_sources.txt'),
        ('wikipedia', '/home/ryan/wbtools/Japanese/kanji/data/frequency/yatskov_wikipedia_kanji.txt'),
        ('yatskov_novels', '/home/ryan/wbtools/Japanese/kanji/data/frequency/yatskov_novels_kanji.txt')
    ]

# TODO: Generalize this and move it to wb_utilities.py

    for name, file in kanji_files:
        with open(file, mode='r', encoding='utf-8') as infile:
            thelist = infile.readlines()
            for i, v in enumerate(thelist):
                char = v.strip()
                if char not in legitimate_kanji:
                    continue
                char_num = i + 1
                if name == 'edict_common':
                    char_num = True
                if name == 'joyo':
                    char_num = i + 1006  # Accounting for the kyoiku kanji
                if name == 'jinmeiyo':
                    char_num = i + 1006  # Accounting for the kyoiku kanji
                kanjiset.add(char)
                if char not in kanji_dict.keys():
                    kanji_dict[char] = {'char': char, name: char_num}
                else:
                    kanji_dict[char].update({name: char_num})

    kanji_dict = get_integer_value_stats(kanji_dict)
    kanji_dict = get_number_of_integers(kanji_dict)

    return kanji_dict

def write_kanji_files(kanji_list, kanji_dict):
    write_files(entry_type='kanji', dict_data=kanji_dict=[])
    write_json(dict_data=kanji_list, outfile="output/kanji.json"=[])

def connect_mongo_jp():

    # Connect to Mongo instance
    client = MongoClient('mongodb://localhost:27017/')

    # Connect to 'jp' database
    db = client.jp

    return client, db

def main():

    # PARSE KANJIDIC2

    kanji_dict = parse_kanjidic2()

    print(type(kanji_dict))

    # PARSE OTHER DATA
    kanji_dict = collect_kanji_tags(kanji_dict)

    # CONSOLIDATE DICTS AND LISTS

    #list_data = list_of_dicts_to_dict(kanji_list)

    #kanji_dict = {**kanji_dict, **kanjidict, **list_data}

    #kanji_list = dict_values_to_list(kanji_dict)

    # WRITE TO CSV

    fieldnames = ['char', 'trimmed_mean', 'mean', 'median', 'count', 'stroke_count',
    'aozora', 'blogs', 'edict_common', 'gsf', 'heisig', 'henshall', 'jinmeiyo', 
    'jlpt', 'joyo', 'kanjidict', 'kic', 'kklc', 'kyoiku', 'mainichi', 'news', 'novels', 
    'rm', 'rtktwo', 'twitter', 'variety', 'wikipedia', 'yatskov_novels', 'variants',
    'lookalikes', 'pattern', 'radicals', 'components', 'related_kanji', 'bigrams',
    'antonyms', 'dict_numbers']

    csv_file_path='output/kanjiscores.csv'
    write_csv(kanji_dict, csv_file_path, fieldnames=fieldnames, delimiter='\t')

    # Sort the resulting csv file by trimmed_mean
    sort_csv(csv_file_path, delimiter='\t', key_column=2)
    print('Wrote the kanji scores to ' + csv_file_path + '.')

    # WRITE FILES

    write_kanji_files(kanji_list, kanji_dict)

    # WRITE TO JSON

    write_json(kanji_list)

    # UPDATE MONGO

    client, db = connect_mongo_jp()
    client.close()

if __name__=='__main__':
    main()