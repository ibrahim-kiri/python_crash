from pathlib import Path
import json

number = int(input("Enter your favorite number: "))

path = Path('refactor.json')
contents = json.dumps(number)
path.write_text(contents)
