def search_insert(arr, target):
    # Set the search boundaries
    left = 0
    right = len(arr) - 1

    # Search for the target
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    # Target is not present, left is its insert position
    return left


numbers = [1, 3, 5, 6]

result = search_insert(numbers, 4)

print(result)