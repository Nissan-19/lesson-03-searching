def ternary_search(arr, target):
    # Set search boundaries
    left = 0
    right = len(arr) - 1

    # Continue while search space exists
    while left <= right:
        third = (right - left) // 3

        # Find the two dividing indexes
        mid1 = left + third
        mid2 = right - third

        # Check both middle positions
        if arr[mid1] == target:
            return mid1

        if arr[mid2] == target:
            return mid2

        # Search the left region
        if target < arr[mid1]:
            right = mid1 - 1

        # Search the right region
        elif target > arr[mid2]:
            left = mid2 + 1

        # Search the middle region
        else:
            left = mid1 + 1
            right = mid2 - 1

    # Target was not found
    return -1


# Example
numbers = [3, 6, 9, 12, 15, 18, 21, 24, 27]
target = 24

result = ternary_search(numbers, target)

print(result)