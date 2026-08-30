def linear_search(arr, target):
    # Check each element one by one
    for i in range(len(arr)):

        # Return the index if target is found
        if arr[i] == target:
            return i

    # Target was not found
    return -1


numbers = [18, 6, 11, 3, 25, 9]

result = linear_search(numbers, 25)

print(result)