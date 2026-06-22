def find_min_max(arr):
    if not arr: return None, None
    min_val, max_val = arr[0], arr[0]
    for num in arr[1:]:
        if num < min_val: min_val = num
        if num > max_val: max_val = num
    return min_val, max_val
print(find_min_max([5,7,3,4,9,12,6,2]))                 
print(find_min_max([1,3,5,7,9,11,13,15,17]))            
print(find_min_max([22,34,35,36,43,67,12,13,15,17]))    