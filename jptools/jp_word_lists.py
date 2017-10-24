#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

BASE = os.path.expanduser('~/Dropbox/dev/wbtools/Japanese/words/data/')

WORD_CSVS = [
    {'csv_name': 'blogs2008', 'csv_path': str(BASE + 'frequency/jp_blog_freq_2008.tsv')}
]

ORDERED_WORD_LISTS = [
    {'list_name': 'blogs', 'list_path': str(BASE + 'frequency/jp_blog_wordfreq.txt')},
    {'list_name': 'jdict', 'list_path': str(BASE + 'frequency/jdict_word_freq.txt')},
    {'list_name': 'kic', 'list_path': str(BASE + 'pedagogical/kic_words.txt')},
    {'list_name': 'leeds', 'list_path': str(BASE + 'frequency/leeds_freq.txt')},
    {'list_name': 'mainichi', 'list_path': str(BASE + 'frequency/mainichi_word_freq.txt')},
    {'list_name': 'rmjf', 'list_path': str(BASE + 'mixed/rmjf_words.txt')},
    {'list_name': 'wordbrewery', 'list_path': str(BASE + 'frequency/wb_jp_freq.txt')},
    {'list_name': 'wikipedia', 'list_path': str(BASE + 'frequency/wikipedia_word_freq.txt')}

]

UNORDERED_WORD_LISTS = [
    {'set_name': 'edict_common', 'set_path': str(BASE + 'frequency/edict_common_words.txt')},
    {'set_name': 'rtk_two', 'set_path': str(BASE + 'pedagogical/rtk_two.txt')}

]


def main():
    """

    :return:
    :rtype:
    """
    return locals()

if __name__ == '__main__':
    main()
