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
    pass
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    numberOfAttributes = int(input().strip())

    supportThreshold = float(input().strip())

    result = attributesSet(numberOfAttributes, supportThreshold)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()