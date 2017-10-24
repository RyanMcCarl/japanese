#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import csv
import statistics as stats
import pprint as pp
import networkx as nx
from itertools import permutations
from cjktools import scripts
from setup_jp_word_db import get_japanese_db
BASE_PATH = os.path.expanduser('~/Dropbox/dev/wbtools/japanese/words/data/')
db = get_japanese_db()
import re

jdict_words = {w.strip() for w in open(str(BASE_PATH + 'frequency/jdict_word_freq.txt'), encoding='utf-8').readlines()}
assert len(jdict_words) > 100000


def get_frequency_lists():
    x=0
    os.chdir(BASE_PATH + 'frequency')
    file_names = [re.sub(r'(.txt|jp|word|freq|_)', '', f) for f in os.listdir() if 'freq' in f]
    file_paths = [os.path.abspath(f) for f in os.listdir() if 'freq' in f]
    files = zip(file_names, file_paths)
    freq_list_dict = {}
    for f in files:
        freq_list_dict[f[0]] = [word.strip() for word in open(f[1], encoding='utf-8').readlines()]
        try:
            assert len(set(freq_list_dict[f[0]])) > 5000
        except AssertionError as e:
            print('\n'.join([str(f), f[0], f[1], str(e), str(freq_list_dict[f[0]][:10])]))
            break
    return freq_list_dict

def get_top_word_lists():
    os.chdir(BASE_PATH + 'frequency/jp_top_words')
    file_names = [re.sub(r'(jp_top_|.txt)', '', f) for f in os.listdir() if 'txt' in f]
    file_paths = [os.path.abspath(f) for f in os.listdir() if 'txt' in f]
    files = zip(file_names, file_paths)
    top_word_lists_dict = {}
    for f in files:
        top_word_lists_dict[f[0]] = [word.strip() for word in open(f[1], encoding='utf-8').readlines()]
        try:
            assert len(set(top_word_lists_dict[f[0]])) > 999
        except AssertionError as e:
            print('\n'.join([str(f), f[0], f[1], str(e), str(top_word_lists_dict[f[0]][:10])]))
            break
    return top_word_lists_dict

def update_top_word_lists(freq_lists, top_word_files):
    #for num in top_word_files.keys():
    #    print(num)
    #    print(top_word_files[num][:10])
    pass

def filter_words_not_in_jdict(freq_list_dict):
    for listname in freq_list_dict.keys():
        freq_list_dict[listname] = list(filter(lambda x: x in jdict_words, freq_list_dict[listname]))
        #lookinto = set()
        #for word in (freq_list_dict[listname]):
            #if word not in jdict_words:
             #   lookinto.add(word)
        #print('Total in {}: {}'.format(listname, str(len(freq_list_dict[listname]))))
        #print('Not in jdict {}: {}'.format(listname, str(len(lookinto))))
    #for alist in freq_list_dict.keys():
        #print(str(len(freq_list_dict[alist])))
    #    pass
    return freq_list_dict
    #print(sorted(list(lookinto)))

def create_word_dict(freq_list_dict):
    word_dict = {}
    for listname in freq_list_dict.keys():
        for rank, word in enumerate(freq_list_dict[listname], start=1):
            if rank > 30000:
                break
            try:
                word_dict[word].update({listname: rank})
                word_dict[word].update({'count': word_dict[word]['count'] + 1})
                value_list = get_word_stats(word_dict[word])
                #print(word + '\t' + str(value_list))
                word_dict[word].update({'average': round(stats.mean(value_list))})
                word_dict[word].update({'min_rank': min(value_list)})
                word_dict[word].update({'max_rank': max(value_list)})
            except KeyError as e:
                word_dict[word] = {'word': word, listname: rank, 'average': rank, 'count': 1,
                                   'min_rank': rank, 'max_rank': rank,
                                   'chars': sorted(set(c for c in word))}

    print(len(word_dict.keys()))
    return word_dict

def get_word_stats(word_inner_dict):
    assert isinstance(word_inner_dict, dict)
    value_list = []
    lists = ['jdict', 'wb', 'rmjf', 'edict', 'mainichi', 'blogs', 'wikipedia']
    for listname in lists:
        try:
            value_list.append(word_inner_dict[listname])
        except KeyError as e:
            pass
    return value_list

def filter_outliers(word_dict):
    set_to_delete = set()
    for w in word_dict.copy().keys():
        if word_dict[w]['count'] < 4:
            del word_dict[w]
        elif word_dict[w]['min_rank'] > 30000:
            del word_dict[w]
    return word_dict

    #word_dict = {k: v for k, v in word_dict.items() if word_dict[k]['count'] > 3}
    #word_dict = {k: v for k, v in word_dict.items() if word_dict[k]['average'] < 30001}
    #word_dict = {k: v for k, v in word_dict.items() if word_dict[k]['average'] < 30001}
    #return word_dict


def print_top_words(word_list, word_dict):
    for w in word_list:
        pp.pprint([w,
                   word_dict[w]['count'],
                   word_dict[w]['average'],
                   word_dict[w]['min_rank'],
                   word_dict[w]['max_rank']])

def write_word_list_to_csv(word_dict):
    with open(str(BASE_PATH + 'jp_word_data.csv'), 'w', encoding='utf-8', newline='') as outfile:
        fieldnames = ['word', 'average', 'count', 'min_rank', 'max_rank']
        writer = csv.DictWriter(outfile, delimiter='\t', fieldnames=fieldnames)
        writer.writeheader()
        for word in get_sorted_word_list(word_dict):
            writer.writerow({field:word_dict[word][field] for field in fieldnames})
    print('Wrote CSV file of results to ' + BASE_PATH + 'jp_word_data.csv')

def get_sorted_word_list(word_dict):
    # Sort by average, then count (secondary sort), then min_rank (tertiary sort).
    s = sorted(list(word_dict), key=lambda x: word_dict[x]['min_rank'])
    s = sorted(s, key=lambda x: word_dict[x]['count'])
    return sorted(s, key=lambda x: word_dict[x]['average'])

def update_word_db(word_dict):
    for rank, word in enumerate(get_sorted_word_list(word_dict), start=1):
        db.words.update({'word': word}, {'$set': {'rm_rank': rank}}, upsert=True)
        db.words.update({'word': word},
                        {'$set': {'chars': sorted(set(c for c in word))}}, upsert=True)
        for k,v in word_dict[word].items():
            db.words.update({'word': word}, {'$set': {k:v}}, upsert=True)

def update_kanji_db():
    for rank, word in enumerate(get_common_word_list(), start=1):
        for char in scripts.unique_kanji(word):
            if rank <= 500:
                db.kanji.update({'char': char}, {'$addToSet': {'top500words': word}},
                                upsert=True)
            elif rank <= 1000:
                db.kanji.update({'char': char}, {'$addToSet': {'top1000words': word}},
                                upsert=True)
            elif rank <= 3000:
                db.kanji.update({'char': char}, {'$addToSet': {'top3000words': word}},
                                upsert=True)
            elif rank <= 5000:
                db.kanji.update({'char': char}, {'$addToSet': {'top5000words': word}},
                                upsert=True)
            elif rank <= 10000:
                db.kanji.update({'char': char}, {'$addToSet': {'top10000words': word}},
                                upsert=True)
            elif rank <= 15000:
                db.kanji.update({'char': char}, {'$addToSet': {'top15000words': word}},
                                upsert=True)
            elif rank <= 20000:
                db.kanji.update({'char': char}, {'$addToSet': {'top20000words': word}},
                                upsert=True)
            else:
                break

def get_word_freq_dict():
    freq_list_dict = get_frequency_lists()
    freq_list_dict = filter_words_not_in_jdict(freq_list_dict)
    word_dict = create_word_dict(freq_list_dict)
    word_dict = filter_outliers(word_dict)
    return word_dict

def get_common_word_list():
    word_dict = get_word_freq_dict()
    return get_sorted_word_list(word_dict)

def create_kanji_graph(word_dict=get_word_freq_dict()):
    kgraph = nx.Graph()
    #word_dict = get_word_freq_dict()
    for rank, word in enumerate(get_common_word_list(), start=1):
        charpairs = permutations(scripts.unique_kanji(word_dict[word]['chars']), 2)
        wordweight = get_word_importance_by_rank(rank)
        for char1, char2 in charpairs:
            try:
                kgraph[char1][char2]['words'].append((word, rank))
                word_list = sorted(set(kgraph[char1][char2]['words']))
                weight = kgraph[char1][char2]['weight'] - wordweight
                kgraph.add_edge(char1, char2, words=word_list, weight=weight)
            except KeyError:
                kgraph.add_edge(char1, char2, words=[(word, rank)], weight=-wordweight)

    os.chdir(BASE_PATH)
    with open('output/kanji_graph_data.txt', 'w', encoding='utf-8') as outfile:
        outfile.write("#Kanji Graph Data\n\n## DEGREE:\n\n")
        outfile.write(pp.pformat(sorted(kgraph.degree, key=lambda x: x[1], reverse=True)))
        outfile.write("\n\n##CONNECTED COMPONENTS:\n\n")
        outfile.write(pp.pformat(sorted(nx.connected_components(kgraph), key=len, reverse=True)))
        outfile.write("\n\n##CLUSTERING:\n\n")
        outfile.write(pp.pformat(sorted(nx.clustering(kgraph), reverse=True)))
        outfile.write("\n\n##CENTRALITY:\n\n")
        outfile.write(pp.pformat(sorted(nx.betweenness_centrality(kgraph), reverse=True)))
        outfile.write("\n\n##EDGES:\n\n")
        outfile.write(pp.pformat(sorted(kgraph.edges(data=True), key=lambda x: x[1], reverse=True)))
        outfile.write("\n\n##MINIMUM SPANNING TREE:\n\n")
        outfile.write(pp.pformat(sorted(nx.minimum_spanning_tree(kgraph).edges(data=True))))
        print('Wrote graph data to ' + BASE_PATH + 'output/kanji_graph_data.txt')

    return kgraph

def get_word_importance_by_rank(rank):
    if rank <= 500:
        return 5
    elif rank <= 1000:
        return 4
    elif rank <= 5000:
        return 3
    elif rank <= 10000:
        return 2
    elif rank <= 20000:
        return 1
    else:
        return 0

def main():
    #word_dict = get_word_freq_dict()
    #sorted_words = get_sorted_word_list(word_dict)
    #print_top_words(sorted_words[:100], word_dict)
    # top_word_file_dict = get_top_word_lists()
    # update_top_word_lists(freq_list_dict, top_word_file_dict)
    #write_word_list_to_csv(word_dict)
    #update_word_db(word_dict)
    update_kanji_db()
    #create_kanji_graph()
    pass

main()




    #pp.pprint(db.words.find_one({'jdict': {'$lt': 500}}, {'_id':0}))
    #pp.pprint(db.kanji.find_one({'kanjidic': {'$lt': 500}}, {'_id':0}))
    #res = db.words.find({'blogs_2008': {'$exists': True}})
    #    blog = word['blogs_2008']
    #    db.words.update({'word': word}, {'$set': {'blogs': blog}})

    #db.words.update({'blogs_2008': {'$exists': True}}, {'$unset': {'blogs_2008': ''}})

if __name__ == '__main__':
    main()
