from pathlib import Path

contents = input("Enter your name: ")
path = Path("guest.txt")
path.write_text(contents)