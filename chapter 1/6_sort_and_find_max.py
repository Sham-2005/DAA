def process_list(nums):
    if not nums:
        return "List is empty"
    nums.sort()
    return nums[-1]

print(process_list([]))              
print(process_list([5]))             
print(process_list([3, 3, 3]))