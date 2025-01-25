import random
import time
import numpy as np

# Custom Heapsort Implementation
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapsort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# Custom Merge Sort Implementation
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# Custom Quicksort Implementation
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Timing Function
def time_algorithm(func, arr):
    start_time = time.time()
    func(arr)
    return time.time() - start_time

# Generate Input Arrays
def generate_inputs(size):
    return {
        "sorted": list(range(size)),
        "reverse_sorted": list(range(size, 0, -1)),
        "random": random.sample(range(size * 10), size),
    }

# Main Testing
if __name__ == "__main__":
    sizes = [10**3, 10**4, 10**5, 10**6]
    algorithms = {
        "Heapsort": heapsort,
        "Merge Sort": merge_sort,
        "Quicksort": lambda arr: quicksort(arr.copy()),  # Copy for immutability
        "Timsort (Python Built-in)": lambda arr: sorted(arr.copy()),
    }

    for size in sizes:
        print(f"\nArray Size: {size}")
        inputs = generate_inputs(size)

        for algo_name, algo_func in algorithms.items():
            for dist_name, arr in inputs.items():
                # Copy the input array to avoid mutation
                arr_copy = arr.copy()
                exec_time = time_algorithm(algo_func, arr_copy)
                print(f"{algo_name} ({dist_name}): {exec_time:.6f} seconds")
