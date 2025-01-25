def heapify(arr, n, i):
    """
    Maintains the max-heap property for the array.
    :param arr: List of elements
    :param n: Size of the heap
    :param i: Index of the current node
    """
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than the current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)  # Recursively heapify the affected sub-tree


def heapsort(arr):
    """
    Heapsort algorithm implementation.
    :param arr: List of elements to be sorted
    """
    n = len(arr)

    # Build a max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap the current root with the end element
        heapify(arr, i, 0)  # Heapify the reduced heap


# Example usage
if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9,0,11,34,55,66,77,12]
    print("Original array:", arr)
    heapsort(arr)
    print("Sorted array:", arr)
