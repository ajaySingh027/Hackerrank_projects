#!/bin/python3

import math
import os
import random
import re
import sys

import pandas as pd
import numpy as np
from collections import OrderedDict

url = 'https://s3.amazonaws.com/istreet-questions-us-east-1/443606/census.csv'

df = pd.read_csv(url, header=None)

def arrangingRules(rules):
    
    confidn = {}
    
    for rule in rules:
        iter = 0
        X = 0
        XY = 0
        temp_df = df
        print(rule + ": ----")
        sub_list = rule.split('=>')
        for item in sub_list:
            str_1 = item.strip('{}')
            list_2 = str_1.split(',')
            
            # Support value for list_2
            if iter == 0:
                temp_df, X = len_stringSearch(temp_df, list_2)
                print("X:-- " + str(X))
            else:
                temp_df, XY = len_stringSearch(temp_df, list_2)
                print("XY:-- " + str(XY))
            
            iter += 1
        
        
        # Adding the confidence value for each rule to dictionary
        confidn[rule] = (XY / X)
    
    # Sorting the dictionary keys in descending order -----
    res_descending = OrderedDict(sorted(confidn.items(), key=lambda kv: kv[1], reverse=True))
    result = [x for x in res_descending.keys()]

    return result

    

def count_val(df, text):
    '''
    For Counting the specific pattern values in the Dataframe
    '''
    # mask = df.applymap(lambda x: text in str(x))
    # temp_df = df[mask.any(axis=1)]
    mask = np.column_stack([df[col].str.contains(text, na=False) for col in df])
    temp_df = df.loc[mask.any(axis=1)]
    return temp_df, len(temp_df)


def len_stringSearch(df, myList = []):
    '''
    to count the number of rows with specific text(s) in Cells
    '''
    temp_df = df
    for element in myList:
        temp_df, count = count_val(temp_df, element)
    
    return temp_df, count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rules_count = int(input().strip())

    rules = []

    for _ in range(rules_count):
        rules_item = input()
        rules.append(rules_item)

    result = arrangingRules(rules)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()