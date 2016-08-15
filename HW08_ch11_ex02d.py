#!/usr/bin/env python3
# HW08_ch11_ex02d.py
# (1) Write a more concise version of invert_dict_old.

# (2) Paste in your completed functions from HW08_ch11_ex02a.py

# (3) Update print_hist_new from HW08_ch11_ex02b.py to be able to print
# a sorted version of the dict (print key/value pairs from 0 through the
# largest key values, (and those in between))
# Ex. If d = {1:["this, that"], 3: ["the"]}, it prints:
#    '1: ["this", "that"]'
#    '2:'
#    '3: ["the"]'
###############################################################################
# Imports


# Body
def invert_dict_old(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


def invert_dict_new(d):
    pass


def print_hist_newest(h):
    for c in h:
        lst = sorted(h.keys())
    return lst

###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a BELOW: ###########################
###############################################################################

pledge_histogram = {}


def histogram_old(s):
    d = dict()
    for c in s:
        d.get(c, 0)
    return d


def histogram_new(list_):
    dict_new = {word: list_.count(word) for word in list_}
    return dict_new


def get_pledge_list():
    """ Opens pledge.txt and converts to a list, each item is a word in
    the order it appears in the original file. returns the list.
    """
    # Your code here.
    with open('pledge.txt', 'r') as fin:
        pledge_list = []
        for line in fin.readlines():
            pledge_list.extend(line.split())

#        pledge_list = [line.split() for line in fin.readlines()]
    return pledge_list


# def print_hist_newsest(h):
#     for c in h:
#         lst = sorted(h.keys())
#     return lst
###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a BELOW: ###########################
###############################################################################
def main():  # DO NOT CHANGE BELOW
    pledge_histogram = histogram_new(get_pledge_list())
    pledge_invert = invert_dict_new(pledge_histogram)
    print_hist_newest(pledge_invert)

if __name__ == '__main__':
    main()
