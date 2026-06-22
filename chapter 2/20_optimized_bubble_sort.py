def bubble_sort_optimized(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Test Cases [cite: 8]
print(bubble_sort_optimized([64, 25, 12, 22, 11])) 
print(bubble_sort_optimized([1, 2, 3, 4, 5]))      