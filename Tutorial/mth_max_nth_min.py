def mth_max_nth_min(arr,m,n):
    if m<0 or n<0:
        return "Index must be non negative numbers"
    if m>len(arr) or n>len(arr):
        return "Index out of range"
    arr.sort()
    mth_max=arr[-m]
    nth_min=arr[n-1]
    return mth_max,nth_min
size=int(input("Enter the size of the array: "))
arr=[]
for i in range(size):
    ele=int(input("Enter the element: "))
    arr.append(ele)
m=int(input("Enter the m value for mth max: "))
n=int(input("Enter the n value for nth min: "))
mth_max,nth_min=mth_max_nth_min(arr,m,n)
print(f"{m}th maximum element is: {mth_max}")
print(f"{n}th minimum element is: {nth_min}")