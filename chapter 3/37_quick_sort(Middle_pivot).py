def quick_sort_mid(arr):
    if len(arr) <= 1: return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    print(f"Partition -> Left: {left} Mid: {middle} Right: {right}")
    return quick_sort_mid(left) + middle + quick_sort_mid(right)
print("Sorted:", quick_sort_mid([19,72,35,46,58,91,22,31]))