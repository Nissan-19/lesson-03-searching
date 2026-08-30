numbers = [4, 2, 4, 1, 2, 4]

frequency = {}

# Count how many times each number appears
for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1

print(frequency)