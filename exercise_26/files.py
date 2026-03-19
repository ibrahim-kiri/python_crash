from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()
content = contents.replace('Python', 'C')
print(content)

learn_py = ''
for line in content.splitlines():
    learn_py += line
print(learn_py)
