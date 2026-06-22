def subset_sum(numbers,target):
    n=len(numbers)
    numbers.sort()
    def backtrack(index,current_path,current_sum):
        if current_sum==target:
            return current_path
        if current_sum>target or index==n:
            return None
        if current_sum+numbers[index]<=target:
            result=backtrack(index+1, current_path+[numbers[index]],current_sum+numbers[index])
            if result:return result
        result=backtrack(index+1, current_path,current_sum)
        if result:return result
        return None
    return backtrack(0,[],0)
nums=[3,34,4,12,5,2]
target=9
print(subset_sum(nums,target))