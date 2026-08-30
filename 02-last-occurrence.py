def last_occurrence(arr, target):
    # Search from the end of the array
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == target:
            return i

    # Target was not found
    return -1


numbers = [4, 7, 2, 7, 9, 7]

result = last_occurrence(numbers, 7)

print(result)