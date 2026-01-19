name = 'Eric rambo'
print(f'Hello {name}, would you like to learn some Python today?')

print(name.lower())
print(name.upper())
print(name.title())

famous_name = 'Albert Einstein'
message = 'once said, "A person who never made a mistake never tried anything new."'
print(f'{famous_name} {message}')

strip_name = " John "
print(f'\t{strip_name.lstrip()}')
print(f'\n{strip_name.rstrip()}')
print(f'\n{strip_name.strip()}')

filename = 'python_notes.txt'
print(filename.removesuffix('.txt'))