def calculate_indices_counts(nums1, nums2):
    set1, set2 = set(nums1), set(nums2)
    ans1 = sum(1 for x in nums1 if x in set2)
    ans2 = sum(1 for x in nums2 if x in set1)
    
    return [ans1, ans2]

print(calculate_indices_counts([4,3,2,3,1], [2,2,5,2,3,6])) 