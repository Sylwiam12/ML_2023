#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv

from typing import Dict
import pandas as pd


def get_vocabulary_dict() -> Dict[int, str]:
    """Read the fixed vocabulary list from the datafile and return.

    :return: a dictionary of words mapped to their indexes
    """

    # FIXME: Parse data from the 'data/vocab.txt' file.
    # - The file is saved in tab-separated values (TSV) format.
    # - Each line contains a word's ID and the word itself.
    # The output dictionary should map word's ID on the word itself, e.g.:
    #   {1: 'aa', 2: 'ab', ...}
    path="./lab6/svm_spam__skeleton/data/vocab.txt"
    df = pd.read_csv(path, sep='\t',encoding='utf-8',names=['nr','word'],header=None)
    dictionary=df.set_index('nr').to_dict(orient='dict')
    return dictionary['word']
