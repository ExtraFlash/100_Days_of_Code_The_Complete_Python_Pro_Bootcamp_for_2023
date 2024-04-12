import pandas as pd

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_dataframe = pd.DataFrame(data=student_dict)
# print(student_dataframe)

# Loop through a data frame
# for (key ,value) in student_dataframe.items():
#     print(value)

# Loop through rows of a data frame
for (index, row) in student_dataframe.iterrows():
    print(row.student)
