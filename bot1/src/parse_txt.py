# -*- coding: utf-8 -*-
import json

import codecs


def parse(file):
    '''
    (str) -> json.file

    Return .json file from .txt file
    '''
    input_file = open(file, 'r', encoding='utf-8')
    _dict_ = {}
    for each in input_file.readlines():
        each = each.strip().split('/')
        # print(each)
        tup1 = each[1]
        tup2 = tuple(i for i in each[2].split(";"))
        _dict_[each[0]] = (tup1, tup2)
    with codecs.open('./datastorage/history.json', 'w', encoding='utf-8') as f:
        json.dump(_dict_, f, ensure_ascii=False)

parse('hist.txt')
