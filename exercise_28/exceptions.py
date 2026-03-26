print("Give me two numbers and i'll add them.")
print("Type 'q' to quit.")

while True:
    first_number = input("Enter first number: ")
    if first_number == 'q':
        break
    second_number = input("Enter second number: ")
    if second_number == 'q':
        break

    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("You can not add strings")
    else:
        print(answer)