#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Get kana
"""
Return a list of kana.

.. moduleauthor:: Ryan McCarl <admin@wordbrewery.com>

"""
def main():
    katakana = [k.strip() for k in open('Japanese/kana/hiragana_order.txt').read()]
    hiragana = [k.strip() for k in open('Japanese/kana/katakana_order.txt').read()]
    kana = set(hiragana) | set(katakana)
    assert len(kana) > 150
    return {'hiragana': hiragana, 'katakana': katakana, 'kana': kana}

if __name__ == '__main__':
    main()