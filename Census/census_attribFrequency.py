#!/bin/python3

import math
import os
import random
import re
import sys

import pandas as pd
import itertools

# df = pd.read_csv('census.csv', header=None)
url = 'https://s3.amazonaws.com/istreet-questions-us-east-1/443605/census.csv'
df = pd.read_csv(url, header=None)
# print(df)

# New df for storing the unique rows data
df_unique = df.drop_duplicates()

# len(df.drop_duplicates())

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


def finalSupport(full_list, threshold):
    '''
    To scan each item in list and compare with threshold value to retain it
    '''
    # Final list to contain the combinations
    finalList = []
    for item in full_list:
        support = 0
        temp_df, count = len_stringSearch(df, item)
        support = count / len(df)
        if support >= threshold:
            finalList.append(item)
    
    return finalList


def len_stringSearch(df, myList = []):
    '''
    to count the number of rows with specific text(s) in Cells
    '''
    temp_df = df
    for element in myList:
        temp_df, count = count_val(temp_df, element)
    
    return temp_df, count


def count_val(df, text):
    '''
    For Counting the specific pattern values in the Dataframe
    '''
    mask = df.applymap(lambda x: text in str(x))
    temp_df = df[mask.any(axis=1)]
    return temp_df, len(temp_df)

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    numberOfAttributes = int(input().strip())

    supportThreshold = float(input().strip())

    result = attributesSet(numberOfAttributes, supportThreshold)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()