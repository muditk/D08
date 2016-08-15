#!/usr/bin/env python3
# HW08_ch11_ex02b
# This borrows from exercise two in the book.
# Dictionaries have a method called keys that returns the keys of the
# dictionary, in no particular order, as a list.

# (1) Modify print_hist_old to print the keys and their values in alphabetical
# order.

# (2) Paste in your completed functions from HW08_ch11_ex02a.py

# (3) Within main() make the appropriate function calls to print the
# alphabetical histogram of pledge.txt
###############################################################################
# Imports


# Body
def print_hist_old(h):
    for c in h:
        lst = sorted(h.keys())
    return lst


def print_hist_new(h):
    pass


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


###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a BELOW: ###########################
###############################################################################
def main():
    """ Calls print_hist_new with the appropriate arguments to print the
    histogram of pledge.txt.
    """
    pledge_histogram = histogram_new(get_pledge_list())
    print(print_hist_old(pledge_histogram))

if __name__ == '__main__':
    main()
