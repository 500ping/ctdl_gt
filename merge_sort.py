# MergeSort in Python

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = []
    R = []
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L.append(arr[l + i])
 
    for j in range(0, n2):
        R.append(arr[m + 1 + j])

    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
    # l is for left index and r is right index of the
    # sub-array of arr to be sorted


def merge_sort(array, l, r):
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
 
        # Sort first and second halves
        merge_sort(array, l, m)
        merge_sort(array, m+1, r)
        merge(array, l, m, r)

# Driver program
if __name__ == '__main__':
    array = [6, 5, 12, 10, 9, 1]
    print('Array:', array)

    merge_sort(array, 0, len(array) - 1)

    print("Sorted array is:", array)