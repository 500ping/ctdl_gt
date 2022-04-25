def binary_search(target, arr, first, last):
    if first > last:
        return -1
    else:
        mid = (first + last) // 2
        if target < arr[mid]:
            return binary_search(target, arr, first, mid - 1)
        elif target > arr[mid]:
            return binary_search(target, arr, mid + 1, last)
        else:
            return mid
        
    # while first <= last:
    #     mid = first + (last - first) // 2
    #     if arr[mid] == target:
    #         return mid
    #     elif arr[mid] < target:
    #         first = mid + 1
    #     else:
    #         last = mid - 1
    # return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6
print(arr.index(6))
print(binary_search(6, arr, 0, len(arr) - 1))