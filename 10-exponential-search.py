def binary_search(arr, target, left, right):
    # Search inside the given range
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def exponential_search(arr, target):
    # Empty array
    if len(arr) == 0:
        return -1

    # Check the first element
    if arr[0] == target:
        return 0

    # Grow the search range exponentially
    index = 1

    while index < len(arr) and arr[index] < target:
        index *= 2

    # Binary search inside the discovered range
    left = index // 2
    right = min(index, len(arr) - 1)

    return binary_search(arr, target, left, right)


# Example
numbers = [2, 4, 7, 10, 13, 16, 19, 22, 25, 28]
target = 19

result = exponential_search(numbers, target)

print(result)