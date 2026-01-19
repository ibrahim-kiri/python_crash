guest = ['john', 'mary', 'jane']
print(f"Hi {guest[0]} your invited for dinner at our house.")
print(f"Hi {guest[1]} your invited for dinner at our house.")
print(f"Hi {guest[2]} your invited for dinner at our house.")

print(f"{guest[0]} cant make to dinner")
guest.insert(0, 'caro')
print(f"Hi {guest[0]} your invited for dinner at our home.")
print(f"Hi {guest[1]} your invited for dinner at our home.")
print(f"Hi {guest[2]} your invited for dinner at our home.")

message = "I have found a bigger table, we can invite more friends"
print(f"{guest[0]}, {guest[1]}, {guest[2]}, {message}")
guest.insert(0, 'karen')
guest.insert(1, 'kathy')
guest.append('paul')
print(f"Hi {guest[0]} your invited for dinner at our home.")
print(f"Hi {guest[1]} your invited for dinner at our home.")
print(f"Hi {guest[2]} your invited for dinner at our home.")
print(f"Hi {guest[3]} your invited for dinner at our home.")
print(f"Hi {guest[4]} your invited for dinner at our home.")
print(f"Hi {guest[5]} your invited for dinner at our home.")
print(f"Hi {guest[6]} your invited for dinner at our home.")

message2 = "For now i can only invite two friends for dinner"
print(message2)
guest.pop(0)
print(f"Hi {guest[0]}, we are sorry your not invited")

guest.pop(1)
print(f"Hi {guest[1]}, we are sorry your not invited")

guest.pop(2)
print(f"Hi {guest[2]}, we are sorry your not invited")

print(f"Hi {guest[3]}, you still invited to our home")

del guest[0]
del guest[1]
print(guest)
print(len(guest))


