from pathlib import Path

path = Path("guest_book.txt")

while True:
    contents = input("Enter your name (or 'q' to quit): ")

    if contents == 'q':
        print("You're done writing to the file.")
        break

    with path.open("a") as file:
        file.write(contents + "\n")