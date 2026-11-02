import random
import time

# Deterministic Quick Sort
def deterministic_quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    left = []
    right = []

    for i in arr[1:]:
        if i <= pivot:
            left.append(i)
        else:
            right.append(i)

    return deterministic_quick_sort(left) + [pivot] + deterministic_quick_sort(right)


# Randomized Quick Sort
def randomized_quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]

    left = []
    right = []

    for i in range(len(arr)):
        if i != pivot_index:
            if arr[i] <= pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])

    return randomized_quick_sort(left) + [pivot] + randomized_quick_sort(right)


# Main Program
n = int(input("Enter number of elements: "))

if n <= 0:
    print("Enter a positive number")

else:
    arr = list(map(int, input("Enter array elements: ").split()))

    if len(arr) != n:
        print("Please enter exactly", n, "elements")

    else:
        # Deterministic Quick Sort
        start = time.perf_counter()
        result1 = deterministic_quick_sort(arr.copy())
        end = time.perf_counter()

        time1 = end - start

        # Randomized Quick Sort
        start = time.perf_counter()
        result2 = randomized_quick_sort(arr.copy())
        end = time.perf_counter()

        time2 = end - start

        print("\nDeterministic Quick Sort:")
        print("Sorted Array:", result1)
        print("Execution Time:", time1, "seconds")

        print("\nRandomized Quick Sort:")
        print("Sorted Array:", result2)
        print("Execution Time:", time2, "seconds")




# Sample Input and Output
# Input
# Enter number of elements: 6
# Enter array elements: 45 12 89 3 25 10


# Expected output format
# Deterministic Quick Sort:
# Sorted Array: [3, 10, 12, 25, 45, 89]
# Execution Time: ... seconds

# Randomized Quick Sort:
# Sorted Array: [3, 10, 12, 25, 45, 89]
# Execution Time: ... seconds