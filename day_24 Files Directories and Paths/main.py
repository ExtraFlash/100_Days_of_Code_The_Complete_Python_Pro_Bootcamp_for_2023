# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# with open("new_file.txt", mode='w') as file:
#     file.write("New text.")

# new_file.txt is in Desktop. Absolute file path
with open("/Users/Or/Desktop/new_file.txt") as file:
    content = file.read()
    print(content)

# new_file.txt is in Desktop. Relative file path
with open("../../../Desktop/new_file.txt") as file:
    content = file.read()
    print(content)

# in relative path: path = 'plots/my_plot.png'
# in absolute path: path = '/Users/my_name/ ... /my_plots.png'
