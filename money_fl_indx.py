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


def posMoneyFlow():
    pass


def negMoneyFlow():
    pass


def posMoneyFlowSum():
    pass


def negMoneyFlowSum():
    pass



if __name__ == '__main__':
    filename = input()
    n = int(input())
    moneyFlowIndex(filename, n)