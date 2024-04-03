# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     # temperatures = [row[1] for row in data]
#     print(temperatures)


import pandas as pd

# data = pd.read_csv("weather_data.csv")
# # print(type(data))
# # print(type(data["temp"]))
# data_dict = data.to_dict()
# # print(data_dict)
#
# temp_list = data['temp'].to_list()
# # print(temp_list)
#
# # print(data['temp'].mean())
# # print(data['temp'].max())
#
# # get data in columns
# # print(data['condition'])
# # print(data.condition)
#
# # get data in rows
# # print(data[data.day == "Monday"])
#
# # get the row data where the temperature is at the maximum
# temp_max = data.temp.max()
# # print(data.temp == temp_max)
# print(data[data.temp == temp_max])
#
# # this is equivalent
# # ser = pd.Series([False, False, False, False, False, False, True])
# # print(ser)
# # print(data[ser])
#
# monday = data[data.day == 'Monday']  # DataFrame
# monday_temp = monday.temp[0]  # get first value in Series
# monday_temp_F = monday_temp * 9 / 5 + 32
# print(monday_temp_F)
#
# # Create a dataframe from scratch
# data_dict = {
#     "students": ['Amy', 'James', 'Angela'],
#     "scores": [76, 56, 65]
# }
#
# data = pd.DataFrame(data=data_dict)
# data.to_csv("new_data.csv")
