def binary_search(arr, target):
    # Set the search boundaries
    left = 0
    right = len(arr) - 1

    # Continue while there is still a search space
    while left <= right:
        mid = (left + right) // 2

        # Target found
        if arr[mid] == target:
            return mid

        # Search the right half
        elif arr[mid] < target:
            left = mid + 1

        # Search the left half
        else:
            right = mid - 1

    # Target was not found
    return -1


numbers = [2, 5, 8, 12, 16, 23, 30]

result = binary_search(numbers, 23)

print(result)