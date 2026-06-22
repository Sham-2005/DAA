def rob(nums):
    if len(nums) == 1: return nums[0]

    def rob_linear(arr):
        rob1, rob2 = 0, 0
        for n in arr:
            new_rob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = new_rob
        return rob2

    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))

print(rob([2, 3, 2]))    
print(rob([1, 2, 3, 1])) 