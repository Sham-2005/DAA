def min_max(arr,low,high):
    if low==high:
        return (arr[low],arr[low])
    if high==low+1:
        if arr[low]<arr[high]:
            return (arr[low],arr[high])
        else:
            return (arr[high],arr[low])
    mid=(low+high)//2
    min_left,max_left=min_max(arr,low,mid)
    min_right,max_right=min_max(arr,mid+1,high)
    final_min=min(min_left,min_right)
    final_max=max(max_left,max_right)
    return (final_min,final_max)
arr1=[5, 7, 3, 4, 9, 12, 6, 2]
n=len(arr1)
minimum,maximum=min_max(arr1,0,n-1)
print("Minimum element is:",minimum)
print("Maximum element is:",maximum)