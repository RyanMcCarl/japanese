#!/usr/env/python
# -*- coding: utf-8 -*-
#
# Get Kanji Bigrams
#
#

def get_word_set():
    words = set()
    with open('Japanese/words/kwat_chars_only.csv') as infile:
        words = words | {w.strip() for w in infile.readlines()}
    with open('Japanese/words/wikipedia_word_freq.txt') as infile:
        words = words | {w.strip() for w in infile.readlines()}
    with open('Japanese/words/rmjf_words.txt') as infile:
        words = words | {w.strip() for w in infile.readlines()}
    with open('Japanese/words/kic_words.txt') as infile:
        words = words | {w.strip() for w in infile.readlines()}
    with open('Japanese/words/mainichi_word_freq.txt') as infile:
        words = words | {w.strip() for w in infile.readlines()}
    with open('Japanese/words/leeds_freq.txt') as infile:
        words = words | {w.strip() for w in infile.readlines()}
    with open('Japanese/words/wb_jp_freq.txt') as infile:
        words = words | {w.strip() for w in infile.readlines()}
    return words


def write_bigrams_file(kanij_dict):
    with open('output/kanji_bigrams.csv', mode='w') as outfile:
        for k,v in kanji_dict.items():
            line = k + '\t' + ''.join(c for c in v) + '\n'
            outfile.writelines(line)


def get_possible_chars(include_kana=False):
    possible = {k.strip() for k in open('Japanese/kanji/data/mixed/rm_2323_kanji.txt', mode='r').readlines()}
    if include_kana == True:
        return possible_set | get_kana()
    return possible


def get_ignored_chars(ignore_kana=True):
        ignore_set = {c.strip() for c in open('Japanese/kanji/data/reference/jp_ignore.txt', mode='r').readlines()}
        if ignore_kana == True:
            return ignore_set | get_kana()
        else:
            return ignore_set


def get_kana():
    kana = {k.strip() for k in open('Japanese/kana/jp_kana.txt', mode='r').readlines()}
    return kana


def get_legitimate_kanji():
    with open('Japanese/kanji/data/mixed/rm_2323_kanji.txt', mode='r', encoding='utf-8') as infile:
        legitimate_kanji = {k.strip() for k in infile.readlines()}
        return legitimate_kanji

def get_char_set_from_word(word=""):
    possible = get_possible_chars()
    ignore = set()#get_ignored_chars()
    chars = {c for c in word if c in possible and c not in ignore}
    return chars

def get_bigrams(kanji_dict={}):
    example_words = {}
    for k in get_legitimate_kanji():
        example_words[k] = set()


    bigrams = {} # {kanji, [bigram1,bigram2...]}
    words = get_word_set()
    for word in words:
        chars = get_char_set_from_word(word)
        for char in chars:
            otherchars = {c for c in chars if c is not char}
            # Add bigrams to new bigrams dictionary
            if char not in set(bigrams.keys()):
                bigrams[char] = otherchars
            else:
                bigrams[char] = sorted(list(set(bigrams[char]) | otherchars))
            example_words[k] = sorted(list(set(example_words[k]) | set(word)))

    with open('output/example_words_by_kanji.csv', mode='w') as outfile:
        for char, words in example_words.items():
            line = str(str(k) + '\t' + ','.join(words) + '\n')
            outfile.writelines(line)

    return bigrams

def main():
    bigrams = get_bigrams()
    write_bigrams_file(bigrams)

if __name__ == '__main__':
    main()