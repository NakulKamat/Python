list = [1, 3, 4, 56, 3, 2, 2, 3, 4, 1, 56]
unique = []
for number in list:
  if number not in unique:
    unique.append(number)
print(unique)