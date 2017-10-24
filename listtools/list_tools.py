#!/usr/bin/env python3

def add_list_to_dict(adict, enumerable_list, listname, boolean=False):
    """
    Add a list of imtes

    :param adict: A python dictionary to which you want to add words
    :type adict: dict
    :param enumerable_list: Generator or list to add to the dictionary
    :type enumerable_list: list
    :param listname: Name of the list you are adding
    :type listname: str
    :param boolean: Set to True to record whether or not a word is present in the list as opposed to its rank. Useful for unordered lists
    :type boolean: bool
    :return: The dictionary you passed in
    :rtype: dict
    """
    for e in enumerable:
        rank = e[0]
        word = e[1]
        try:
            adict[word][listname] = rank
        except:
            adict[word] = {'word': word, listname: rank}
    return adict

if __name__ == '__main__':
    pass
