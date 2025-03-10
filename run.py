import pandas as pd
import os
import csv

dir_path = os.path.abspath(os.path.dirname(__file__))

df = pd.read_csv(os.path.join(dir_path, '10K-bquxjob_1e975433_195807d7dd1.csv'))

print('\n')
print('Most cited patent documents:')
print('-----------------------')
print(df.head(10)) 


# Number of citations per category
cpc_categories = {}

for index, row in df.iterrows():
    if row['code'] in cpc_categories:
        cpc_categories[row['code']] = cpc_categories[row['code']] + row['number_of_cited_by']
    else:
        cpc_categories[row['code']] = row['number_of_cited_by']

# Sort the dictionary by its values in ascending order
sorted_dict = dict(sorted(cpc_categories.items(), reverse = True, key=lambda item: item[1]))

df_2 = pd.DataFrame.from_dict(sorted_dict, orient='index', dtype=None, columns=['number_of_cited_by'])


print('\n')
print('Most cited top CPC categories:')
print('-----------------------')
print(df_2.head(10))

# Number of citations per category (top level)
cpc_categories_top_2 = {}

for index, row in df.iterrows():
    top_category_2 = str(row['code'])[:3]
    if top_category_2 in cpc_categories_top_2:
        cpc_categories_top_2[top_category_2] = cpc_categories_top_2[top_category_2] + row['number_of_cited_by']
    else:
        cpc_categories_top_2[top_category_2] = row['number_of_cited_by']

# Sort the dictionary by its values in ascending order
sorted_dict_2 = dict(sorted(cpc_categories_top_2.items(), reverse = True, key=lambda item: item[1]))

df_4 = pd.DataFrame.from_dict(sorted_dict_2, orient='index', dtype=None, columns=['number_of_cited_by'])

print('\n')
print('Most cited top CPC categories (L2):')
print('-----------------------')
print(df_4.head(10))

# Number of citations per category (top level)
cpc_categories_top = {}

for index, row in df.iterrows():
    top_category = str(row['code'])[:1]
    if top_category in cpc_categories_top:
        cpc_categories_top[top_category] = cpc_categories_top[top_category] + row['number_of_cited_by']
    else:
        cpc_categories_top[top_category] = row['number_of_cited_by']

# Sort the dictionary by its values in ascending order
sorted_dict_3 = dict(sorted(cpc_categories_top.items(), reverse = True, key=lambda item: item[1]))

df_3 = pd.DataFrame.from_dict(sorted_dict_3, orient='index', dtype=None, columns=['number_of_cited_by'])

print('\n')
print('Most cited CPC categories:')
print('-----------------------')
print(df_3.head(10))

with open(os.path.join(dir_path, "README.md"), "w") as f:
    f.write('# Patent Landscaping for Mechanical Engineering')
    f.write('\n\nThe goal of this project is to automate the patent landscaping process in mechanical engineering, in order to quickly identify relevant patent documents and CPC categories from a patent database. We assume, that patent documents, which are cited often, are relevant.\n\n')
    f.write('\n\nThis project includes 10K and 100K entries of patent documents.\n\n')
    f.write('\n\n## Most cited patent documents\n\n')
    f.write(df.head(10).to_markdown(floatfmt='.0f'))
    f.write('\n\n## Most cited CPC categories\n\n')
    f.write(df_2.head(10).to_markdown(floatfmt='.0f'))
    f.write('\n\n## Most cited top CPC categories (L2)\n\n')
    f.write(df_4.head(10).to_markdown(floatfmt='.0f'))
    f.write('\n\n## Most cited top CPC categories\n\n')
    f.write(df_3.head(10).to_markdown(floatfmt='.0f'))



