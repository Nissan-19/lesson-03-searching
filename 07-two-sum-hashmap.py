def two_sum(numbers, target):
    # Store number -> index
    seen = {}

    # Go through each number
    for i in range(len(numbers)):
        current = numbers[i]

        # Find the number needed to reach the target
        complement = target - current

        # If we already saw the complement, return both indexes
        if complement in seen:
            return [seen[complement], i]

        # Remember the current number and its index
        seen[current] = i

    # No valid pair found
    return []


# Example
numbers = [3, 5, 2, 8]
target = 10

result = two_sum(numbers, target)

print(result)