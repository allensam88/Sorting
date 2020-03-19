# TO-DO: complete the helper function below to merge 2 sorted arrays
# 1. While your data set contains more than one item, split it in half
# 2. Once you have gotten down to a single element, you have also *sorted* that element
#    (a single element cannot be "out of order")
# 3. Start merging your single lists of one element together into larger, sorted sets
# 4. Repeat step 3 until the entire data set has been reassembled


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # Base conditions, if one of the arrays doesn't exist, return the other.
    if not arrA:
        return arrB
    if not arrB:
        return arrA

    # check to see if A item is smaller than B item
    if arrA[0] < arrB[0]:
        # add smallest A item to merged_arr and run recursion again with trimmed array
        merged_arr = [arrA[0]] + merge(arrA[1:], arrB)

    # else if B is smaller then A, do the opposite
    else:
        merged_arr = [arrB[0]] + merge(arrA, arrB[1:])
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # base condition, if there is no array, return empty array
    if not arr:
        return []

    # for an array of 1, it's already sorted, return 1st index in the array
    if(len(arr) == 1):
        return [arr[0]]

    # find and establish the midpoint of the array to split it in half
    middle = len(arr) // 2

    # establish the left/right side groupings by self-invoking merge_sort function
    # pass in the arr with everything to the left and then right of midpoint
    left = merge_sort(arr[0:middle])
    right = merge_sort(arr[middle:len(arr)])

    # invoke merge function with left and right arrays
    return merge(left, right)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
