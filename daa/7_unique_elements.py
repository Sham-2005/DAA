def unique_elements(nums):
    seen = set()
    result = []
    for num in nums:
        if num not in seen:
            result.append(num)
            seen.add(num)
    return result
print(unique_elements([3, 7, 3, 5, 2, 5, 9, 2])) # Output: [3, 7, 5, 2, 9]