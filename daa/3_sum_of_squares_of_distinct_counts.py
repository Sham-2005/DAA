def sumCounts(nums):
    total_sum = 0
    n = len(nums)
    for i in range(n):
        distinct_elements = set()
        for j in range(i, n):
            distinct_elements.add(nums[j])
            total_sum += len(distinct_elements) ** 2
    return total_sum

print(sumCounts([1, 2, 1]))