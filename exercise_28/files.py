from pathlib import Path

def cat_names(filename):
    """A method to store cat and dog name"""

    try:
        contents = filename.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
        # print(f"Sorry the file {filename} does not exist.")
    else:
        print(contents)

filenames = ['cat.txt', 'dogs.txt']
for filename in filenames:
    path = Path(filename)
    cat_names(path)