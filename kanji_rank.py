#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Modeling the relationship between kanji to estimate the optimal learning path.

Assumptions:
 All else equal:
  - High-frequency kanji should be studied early.
  - The kanji necessary to read high-frequency words should be studied early.
  - Because of "chunking":
      (a) it is best to study a kanji after having studied all its components/radicals, and
      (b) it is best to study a word after having studied all its kanji characters.

Open questions:
 - Should relatedness between kanji make the weight lower (shortest path problem) or longer (longest path problem)? It seems that shortest path problems are more solvable. So how do I create an inverse relationship between kanjis' "relatedness" and the weight of the edge between them?
 - Should I aim to group kanji, rank them, or both?
 - How should the relatedness between kanji (given kanji A, learn related kanji B and C) interact with absolute criteria such as word frequency (learn high-frequency words first) and stroke order (learn "easy" kanji with fewer strokes first)
 - Is a graph algorithm the best approach?

Possible customizations to add later:
 - Allow user to change the weight of different criteria.
 - Allow users to prioritize kanji from Heisig, KKLC, or Wanikani.

"""

class Kanji(object):
    """
    A kanji object.
    """
    allowed_keys = {'onyomi', 'kunyomi', 'freq', 'words', 'peers', 'stroke_count',
    'radicals', 'components', 'heisig', 'kklc', 'kic', 'wanikani', 'tags', 'grade',
    'known'}

    def __init__(self, char, known=False, **kwargs):
        self.char = char
        self.__dict__.update((k, v) for k, v in kwargs.iteritems() if k in allowed_keys)

    def __str__(self):
        return str(self.char)

    def __repr__(self):
        return str(self.char)

    def get_char(self):
        return str(self.char)


