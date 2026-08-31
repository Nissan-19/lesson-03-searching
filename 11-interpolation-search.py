def interpolation_search(arr, target):
    # Set search boundaries
    left = 0
    right = len(arr) - 1

    # Target must stay inside the current value range
    while (
        left <= right
        and target >= arr[left]
        and target <= arr[right]
    ):
        # Avoid dividing by zero
        if arr[left] == arr[right]:
            if arr[left] == target:
                return left
            return -1

        # Estimate the target's position
        pos = left + (
            (target - arr[left]) * (right - left)
            // (arr[right] - arr[left])
        )

        # Target found
        if arr[pos] == target:
            return pos

        # Search the right side
        elif arr[pos] < target:
            left = pos + 1

        # Search the left side
        else:
            right = pos - 1

    # Target was not found
    return -1


# Example
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
target = 70

result = interpolation_search(numbers, target)

print(result)