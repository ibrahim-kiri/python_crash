for value in range(1, 21):
    print(value)

# for value in range(1, 1_000_000):
#     print(value)

sum_mill = list(range(1, 1_000_000))
mi = min(sum_mill)
ma = max(sum_mill)
su = sum(sum_mill)
print(mi, ma, su)

for value in range(3, 20, 3):
    print(value)

for value in range(1, 31):
    mul = 3 * value
    print(mul)

for value in range(1, 11):
    cub = value ** 3
    print(cub)

cubes = [value ** 3 for value in range(1, 11)]
print(cubes)