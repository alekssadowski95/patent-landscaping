import pandas as pd
import os
import csv


dir_path = os.path.abspath(os.path.dirname(__file__))



os.system('cls') 

print('Patent Landscaping')
print('Aleksander Sadowski (C) 2025')
print('')

command_history = []

# define type of data in patent file
dtype = {
    'publication_number': object,
    'title': object,
    'url': object,
    'code': object,
    'number_of_cited_by': 'int32',
}

# Load entire patent data csv as pandas dataframe
print('Loading patent data...')
#df = pd.read_csv('C:\\Users\\Work\\Downloads\\1M-bq-results-20250310-165622-1741625891242.csv', dtype=dtype)
df = pd.read_csv(os.path.join(dir_path, '1M-bq-results-20250310-165622-1741625891242.csv'), dtype=dtype)
df = df.dropna()

# Load cpc categories
print('Loading cpc categories...')
df_cpc = pd.read_csv(os.path.join(dir_path, 'CPC-bq-results-20250310-215736-1741643875074.csv'))
df_cpc = df_cpc.dropna()

def get_cpc_description(cpc_str):
    pass

os.system('cls') 

print('Patent Landscaping')
print('Aleksander Sadowski (C) 2025')

# remove all rows that contain a NaN
print('\n')
print('Most cited patent documents:')
print('-----------------------')
print(df.head(30))
print('Total patent entries: ' + f"{df.shape[0]:,}")
print('Memory usage: ' + pd.io.formats.info.DataFrameInfo(df).memory_usage_string.strip())

# filter rows by cpc category
while True:    
    print('\n')
    # load command history from file
    with open(os.path.join(dir_path, "history.txt"), "r") as history_file:
        command_history = history_file.readlines()
    print('Last commands:' + str([command[:-1] for command in command_history][-3:]))
    cpc = input('Enter major cpc category: ')
    with open(os.path.join(dir_path, "history.txt"), "a") as history_file:
        history_file.write(cpc + '\n')
    df_temp = df[df['code'].str.startswith(cpc + '/')]
    os.system('cls') 
    print('Patent Landscaping')
    print('Aleksander Sadowski (C) 2025')
    print('')
    print(str(df_temp.shape[0]) + ' Results for CPC "' + cpc + '"')
    print('-----------------------')
    print(df_temp.head(30))
    print('Only showing 30 most cited.')


