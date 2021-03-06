def selection_sort(arr):
    for i in range(len(arr)):
      
        # Find the minimum element in remaining 
        # unsorted array
        min_idx = i
        for j in range(i+1, len(arr)):
            if A[min_idx] > arr[j]:
                min_idx = j
                
        # Swap the found minimum element with 
        # the first element        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

A = [64, 25, 12, 22, 11]
selection_sort(A)
print(A)