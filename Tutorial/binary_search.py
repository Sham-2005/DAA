def binary_search(arr,key):
    arr.sort()
    print("Sorted array is:", arr)
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid]<key:
            low=mid+1
        else:
            high=mid-1
    return -1
print(binary_search([3,9,14,19,25,31,42,47,53], 31))