def median_of_medians(arr, k):
    if len(arr) <= 5:
        arr.sort()
        return arr[k-1]
    sublists = [arr[i:i+5] for i in range(0, len(arr), 5)]
    medians = [sorted(sub)[len(sub)//2] for sub in sublists]
    pivot = median_of_medians(medians, len(medians)//2 + 1)
    
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    equal = [x for x in arr if x == pivot]
    
    if k <= len(low):
        return median_of_medians(low, k)
    elif k <= len(low) + len(equal):
        return pivot
    else:
        return median_of_medians(high, k - len(low) - len(equal))
print(median_of_medians([12, 3, 5, 7, 19], 2)) 