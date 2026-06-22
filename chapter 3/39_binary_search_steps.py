def binary_search_steps(arr, key):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        print(f"Low: {low}, High: {high}, Mid Index: {mid}, Mid Value: {arr[mid]}")
        if arr[mid] == key:
            print(f"Element {key} found at position {mid + 1}")
            return mid + 1
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1
binary_search_steps([3,9,14,19,25,31,42,47,53], 31)