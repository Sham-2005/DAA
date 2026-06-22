def binary_search(arr, key):
    low, high = 0, len(arr) - 1
    comps = 0
    while low <= high:
        comps += 1
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid + 1, comps 
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1, comps
print(binary_search([5,10,15,20,25,30,35,40,45], 20)) 