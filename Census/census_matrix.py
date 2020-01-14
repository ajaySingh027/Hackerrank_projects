import pandas as pd
import numpy as np

df = pd.read_csv('census.csv', header=None)
print(df.head()) 

def arrangingRules(rules):
    # print(rules)
    

def count_val(df, text):
    '''
    For Counting the specific pattern values in the Dataframe
    '''
    mask = df.applymap(lambda x: text in str(x))
    temp_df = df[mask.any(axis=1)]
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