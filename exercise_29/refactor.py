from pathlib import Path
import json

path = Path('refactor.json')
if path.exists():
    contents = path.read_text()
    number = json.loads(contents)
    print(f"I know your favorite number! It's {number}")
else:
    number = int(input("Enter your favorite number: "))
    contents = json.dumps(number)
    path.write_text(contents)