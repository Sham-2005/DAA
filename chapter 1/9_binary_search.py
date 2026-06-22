def binary_search(arr, key):
    arr.sort() 
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return f"Element {key} is found"
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return f"Element {key} is not found"