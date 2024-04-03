import pandas as pd

# Load the squirrel data and create a new csv which contains:
# different furs and for each fur its count

# The way that works given we don't know the set of furs in first place
# squirrel_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# squirrel_counts_dict = {
#     'Fur': [],
#     'Counts': []
# }
# furs_series = squirrel_data['Primary Fur Color']
# furs_set = set(furs_series.to_list())
# print(furs_set)
# for fur in furs_set:
#     if isinstance(fur, str):
#         fur_count = len(squirrel_data[furs_series == fur])
#         squirrel_counts_dict['Fur'].append(fur)
#         squirrel_counts_dict['Counts'].append(fur_count)
#
# squirrel_counts_data = pd.DataFrame(data=squirrel_counts_dict)
# squirrel_counts_data.to_csv("squirrel_count.csv")

# given that we know that the possible furs are: 'Gray',
squirrel_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Gray'])
red_squirrels_count = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Cinnamon'])
black_squirrels_count = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Black'])

data_dict = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
