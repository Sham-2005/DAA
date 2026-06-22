def find_max(nums):
    if not nums:
        return None
    max_val = nums[0]
    for num in nums:
        if num > max_val:
            max_val = num
    return max_val

print(find_max([-10, 2, 3, -4, 5]))