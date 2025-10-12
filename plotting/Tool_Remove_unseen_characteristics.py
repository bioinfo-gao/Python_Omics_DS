import re

def remove_zero_width_spaces(file_path):

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Remove zero-width spaces
    content = re.sub(r'\u200b', '', content)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

# Usage
remove_zero_width_spaces('./plotting/ploting_18_types.ipynb')
