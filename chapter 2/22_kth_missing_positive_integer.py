def findKthPositive(arr, k):
    missing_count = 0
    current = 1
    idx = 0
    while True:
        if idx < len(arr) and arr[idx] == current:
            idx += 1
        else:
            missing_count += 1
            if missing_count == k:
                return current
        current += 1
print(findKthPositive([2,3,4,7,11], 5))  
print(findKthPositive([1,2,3,4], 2))    