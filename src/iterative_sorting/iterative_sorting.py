def selection_sort(arr):
    # Loop through n-1 elements
    for i in range(len(arr)):
        # Start with current index = 0
        cur_index = i
        smallest_index = cur_index
        # For all indices EXCEPT the last index:
        # Loop through elements on right-hand-side of current index
        for item in range(cur_index + 1, len(arr)):
            # Find the smallest element
            if arr[item] < arr[smallest_index]:
                smallest_index = item
        # Swap the element at current index with the smallest element found in above loop
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


def bubble_sort(arr):
    n = len(arr)
    # Loop through your array
    for i in range(n):
        for j in range(0, n - i - 1):
            # Compare each element to its neighbor
            if arr[j] > arr[j + 1]:
                # If elements in wrong position (relative to each other, swap them)
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
