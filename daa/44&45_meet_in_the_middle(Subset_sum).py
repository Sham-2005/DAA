import bisect
def get_sums(arr):
    sums = {0}
    for x in arr:
        sums |= {s + x for s in sums}
    return sorted(list(sums))
def meet_in_middle_closest(arr, target):
    mid = len(arr) // 2
    left = get_sums(arr[:mid])
    right = get_sums(arr[mid:])
    closest = float('inf')
    for l in left:
        rem = target - l
        idx = bisect.bisect_left(right, rem)
        if idx < len(right):
            if abs(target - (l + right[idx])) < abs(target - closest):
                closest = l + right[idx]
        if idx > 0:
            if abs(target - (l + right[idx-1])) < abs(target - closest):
                closest = l + right[idx-1]
    return closest
print(meet_in_middle_closest([45, 34, 4, 12, 5, 2], 42)) 
print(meet_in_middle_closest([1, 3, 9, 2, 7, 12], 15) == 15) 