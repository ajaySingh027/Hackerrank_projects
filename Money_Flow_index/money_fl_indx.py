#!/bin/python3

import pandas as pd
import math, os, random, re, sys


def moneyFlowIndex(filename, n):
    '''
    filename contains the column values as:
    Day, Open, High, Low, Close, Volume 
    '''

    url ='https://s3.amazonaws.com/istreet-questions-us-east-1/433997/sample.csv'
    df = pd.read_csv(url)

    # Creating typical Price column with the calculated values
    df['Typical Price'] = typicalPrice(df['High'], df['Low'], df['Close'])

    


def typicalPrice(high, low, close):
    return (high + low + close)/3


def moneyFlow():
#     df.loc[0, 'Positive Money Flow'] = df.loc[0, 'Typical Price']
#     df.loc[0, 'Negative Money Flow'] = df.loc[0, 'Typical Price']
    df.loc[0, 'Positive Money Flow'] = 0
    df.loc[0, 'Negative Money Flow'] = 0
    
    for i in range(1, len(df)):
        if df.loc[i, 'Typical Price'] > df.loc[i-1, 'Typical Price']:
            df.loc[i, 'Positive Money Flow'] = df.loc[i, 'Typical Price'] * df.loc[i, 'Volume']
        else:
            df.loc[i, 'Positive Money Flow'] = 0

        if df.loc[i, 'Typical Price'] < df.loc[i-1, 'Typical Price']:
            df.loc[i, 'Negative Money Flow'] = df.loc[i, 'Typical Price'] * df.loc[i, 'Volume']
        else:
            df.loc[i, 'Negative Money Flow'] = 0


def MoneyFlowSum():
    return None


if __name__ == '__main__':
    filename = input()
    n = int(input())
    moneyFlowIndex(filename, n)