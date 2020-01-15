#!/bin/python3

import math
import os
import random
import re
import sys

import pandas as pd

df = pd.read_csv('census.csv', header=None)
print(df)

def attributesSet(numberOfAttributes, supportThreshold):
    
    # number of attributes in a combination
    num = numberOfAttributes
    
    full_list = findCombinations(num)
    finalList = finalSupport(full_list, supportThreshold)
    
    return finalList


def findCombinations(num):
    '''
    to find the (num) number of combinations in unique df records
    '''
    
    # Full list to contain all combinations from all rows in df_unique
    full_list = []
    
    for index, row in df_unique.iterrows():
        full_list.extend(list(itertools.combinations(row, num)))
        
    # removing the duplicate combinations
    full_list = list(dict.fromkeys(full_list))
    
    return full_list
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    numberOfAttributes = int(input().strip())

    supportThreshold = float(input().strip())

    result = attributesSet(numberOfAttributes, supportThreshold)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()