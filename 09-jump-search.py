import math


def jump_search(arr, target):
    n = len(arr)

    # Set jump size to √n
    step = int(math.sqrt(n))
    previous = 0

    # Jump until we reach or pass the target
    while previous < n and arr[min(step, n) - 1] < target:
        previous = step
        step += int(math.sqrt(n))

        # Target is larger than every element
        if previous >= n:
            return -1

    # Linear search inside the identified block
    while previous < min(step, n):
        if arr[previous] == target:
            return previous

        previous += 1

    # Target was not found
    return -1


# Example
numbers = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
target = 23

result = jump_search(numbers, target)

print(result)