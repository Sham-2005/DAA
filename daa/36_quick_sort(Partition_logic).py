def quick_sort_trace(arr):
    if len(arr) <= 1: return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    print(f"Pivot: {pivot} | Less: {less} | Greater: {greater}")
    return quick_sort_trace(less) + [pivot] + quick_sort_trace(greater)
print("Result:", quick_sort_trace([10,16,8,12,15,6,3,9,5]))