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

    def typicalPrice(high, low, close):
        return (high + low + close)/3


    # Creating Positive & Negative Money Flow
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


    # Creating Positive & Negative Money Flow
    def moneyFlowSum(n):
        # Positive money flow sum
        for idx in range(n, len(df)):
            df.loc[idx, 'Positive Money Flow Sum'] = sum(df['Positive Money Flow'][idx-n+1 : idx+1])
        for ix in range(n):
            df.loc[ix, 'Positive Money Flow Sum'] = 0

        # Negative money flow sum
        for idx in range(n, len(df)):
            df.loc[idx, 'Negative Money Flow Sum'] = sum(df['Negative Money Flow'][idx-n+1 : idx+1])
        for ix in range(n):
            df.loc[ix, 'Negative Money Flow Sum'] = 0


    # Creating Positive & Negative Money Flow
    def mFlowIndex(n):
        '''
        Formula: --
        Money ratio = PMFSum / NMFSum
        Money Flow Index = (Money ratio * 100 )/ (1 + Money ratio)
        '''
        for i in range(n, len(df)):
            moneyRatio = df.loc[i, 'Positive Money Flow Sum'] / df.loc[i, 'Negative Money Flow Sum'] 
            df.loc[i, 'Money Flow Index'] = (moneyRatio * 100) / (1 + moneyRatio)
        
        for ix in range(n):
            df.loc[ix, 'Money Flow Index'] = 0


    # Function calling-----
    # Creating typical Price column with the calculated values
    df['Typical Price'] = typicalPrice(df['High'], df['Low'], df['Close'])
    moneyFlow()
    moneyFlowSum(n)
    mFlowIndex(n)

    # creating output csv file
    newFile =  'money_flow_index_' + str(n) + '.csv'

    return df.to_csv(newFile, sep=',', index=False)       
    
    


if __name__ == '__main__':
    filename = input()
    n = int(input())
    moneyFlowIndex(filename, n)