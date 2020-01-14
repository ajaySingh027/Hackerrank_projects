import pandas as pd
import numpy as np

df = pd.read_csv('census.csv', header=None)
print(df.head()) 

def arrangingRules(rules):
    print(rules)
    

def count_val(df, text):
    '''
    For Counting the specific pattern values in the Dataframe
    '''
    mask = df.applymap(lambda x: text in str(x))
    temp_df = df[mask.any(axis=1)]
    return temp_df, len(temp_df)

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