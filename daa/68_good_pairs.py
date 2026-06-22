def num_identical_pairs(nums):
    count = 0
    freq = {}
    for num in nums:
        if num in freq:
            count += freq[num]
            freq[num] += 1
        else:
            freq[num] = 1
    return count
print(f"Good pairs: {num_identical_pairs([1,2,3,1,1,3])}") 