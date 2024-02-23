PLACEHOLDER = '[name]'

with open("input/Letters/starting_letter.txt") as file:
    starting_letter = file.read()

with open("input/Names/invited_names.txt") as file:
    invited_names = [line.strip() for line in file.readlines()]

for name in invited_names:
    output_file_path = f"Output/ReadyToSend/letter_for_{name}"
    file_content = starting_letter.replace(PLACEHOLDER, name)
    with open(output_file_path, mode='w') as file:
        file.write(file_content)
