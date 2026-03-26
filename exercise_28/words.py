from pathlib import Path

def count_words(filename):
    """Count the approximate number a word appears in a file."""

    try:
        contents = filename.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        # Count the approximate number a word appears in the file:
        words = contents
        num_words = words.lower().count('the ')
        print(f"The file {filename} has about {num_words} 'the' words.")

filenames = ['alice.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)