def merge_sort_count(arr):
    comparisons = [0] 
    def _merge_sort(a):
        if len(a) > 1:
            mid = len(a) // 2
            left = a[:mid]
            right = a[mid:]
            _merge_sort(left)
            _merge_sort(right)
            i = j = k = 0
            while i < len(left) and j < len(right):
                comparisons[0] += 1
                if left[i] < right[j]:
                    a[k] = left[i]
                    i += 1
                else:
                    a[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                a[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                a[k] = right[j]
                j += 1
                k += 1
    _merge_sort(arr)
    return arr, comparisons[0]
arr, comps = merge_sort_count([12,4,78,23,45,67,89,1])
print(f"Sorted: {arr}, Comparisons: {comps}")