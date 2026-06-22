def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print(selection_sort([5, 2, 9, 1, 5, 6]))      
print(selection_sort([10, 8, 6, 4, 2]))        
print(selection_sort([1, 2, 3, 4, 5]))         