def recursive_linear_search(arr, target, index=0):
    # Base case: reached the end of the array
    if index == len(arr):
        return -1

    # Target found
    if arr[index] == target:
        return index

    # Search from the next index
    return recursive_linear_search(arr, target, index + 1)


numbers = [5, 8, 12, 20]

result = recursive_linear_search(numbers, 12)

print(result)