import pandas as pd
import os
import csv

dir_path = os.path.abspath(os.path.dirname(__file__))

# Load entire patent data csv as pandas dataframe
df = pd.read_csv(os.path.join(dir_path, '10K-bquxjob_1e975433_195807d7dd1.csv'))
df = df.dropna()
print('\n')
print('Most cited patent documents:')
print('-----------------------')
print(df.head(10)) 

# Load cpc categories
df_cpc = pd.read_csv(os.path.join(dir_path, 'CPC-bq-results-20250310-215736-1741643875074.csv'))
df_cpc = df_cpc.dropna()
print('\n')
print('CPC categories:')
print('-----------------------')
print(df_cpc.head(10))




cpc_categories = {}

for index, row in df.iterrows():
    if row['code'] in cpc_categories:
        cpc_categories[row['code']] = cpc_categories[row['code']] + row['number_of_cited_by']
    else:
        cpc_categories[row['code']] = row['number_of_cited_by']

# Sort the dictionary by its values in ascending order
sorted_dict = dict(sorted(cpc_categories.items(), reverse = True, key=lambda item: item[1]))


df_2 = pd.DataFrame.from_dict(sorted_dict, orient='index').reset_index()
df_2.columns = ['code', 'number_of_cited_by']

print('\n')
print('Most cited CPC categories:')
print('-----------------------')
df_2_head = df_2.head(10)
description_list = []
for index, row in df_2_head.iterrows():
    results = df_cpc.loc[df_cpc["symbol"] == row["code"]]
    description_list.append(results['titleFull'].values[0])
df_2_head['description'] = description_list
print(df_2_head)



cpc_categories_top_2 = {}

for index, row in df.iterrows():
    top_category_2 = str(row['code'])[:3]
    if top_category_2 in cpc_categories_top_2:
        cpc_categories_top_2[top_category_2] = cpc_categories_top_2[top_category_2] + row['number_of_cited_by']
    else:
        cpc_categories_top_2[top_category_2] = row['number_of_cited_by']

# Sort the dictionary by its values in ascending order
sorted_dict_2 = dict(sorted(cpc_categories_top_2.items(), reverse = True, key=lambda item: item[1]))

df_4 = pd.DataFrame.from_dict(sorted_dict_2, orient='index').reset_index()
df_4.columns = ['code', 'number_of_cited_by']

# Number of citations per category L2
print('\n')
print('Most cited top CPC categories (L2):')
print('-----------------------')
df_4_head = df_4.head(10)
description_list_4 = []
for index, row in df_4_head.iterrows():
    results = df_cpc.loc[df_cpc["symbol"] == row["code"]]
    description_list_4.append(results['titleFull'].values[0])
df_4_head['description'] = description_list_4
print(df_4_head)


cpc_categories_top = {}

for index, row in df.iterrows():
    top_category = str(row['code'])[:1]
    if top_category in cpc_categories_top:
        cpc_categories_top[top_category] = cpc_categories_top[top_category] + row['number_of_cited_by']
    else:
        cpc_categories_top[top_category] = row['number_of_cited_by']

# Sort the dictionary by its values in ascending order
sorted_dict_3 = dict(sorted(cpc_categories_top.items(), reverse = True, key=lambda item: item[1]))

df_3 = pd.DataFrame.from_dict(sorted_dict_3, orient='index').reset_index()
df_3.columns = ['code', 'number_of_cited_by']

# Number of citations per top category
print('\n')
print('Most cited CPC top categories:')
print('-----------------------')
df_3_head = df_3.head(10)
description_list_3 = []
for index, row in df_3_head.iterrows():
    results = df_cpc.loc[df_cpc["symbol"] == row["code"]]
    description_list_3.append(results['titleFull'].values[0])
df_3_head['description'] = description_list_3
print(df_3_head)

with open(os.path.join(dir_path, "README.md"), "w") as f:
    f.write('# Patent Landscaping for Mechanical Engineering')
    f.write('\n\nThe goal of this project is to automate the patent landscaping process in mechanical engineering, in order to quickly identify relevant patent documents and CPC categories from a patent database. We assume, that patent documents, which are cited often, are relevant.\n\n')
    f.write('\n\nThis project includes 10K and 100K entries of patent documents.\n\n')
    f.write('\n\n## Most cited patent documents\n\n')
    f.write(df.head(10).to_markdown(floatfmt=".0f"))
    f.write('\n\n## Most cited CPC categories\n\n')
    f.write(df_2_head.to_markdown(floatfmt='.0f'))
    f.write('\n\n## Most cited top CPC categories (L2)\n\n')
    f.write(df_4_head.to_markdown(floatfmt='.0f'))
    f.write('\n\n## Most cited top CPC categories\n\n')
    f.write(df_3_head.to_markdown(floatfmt='.0f'))



