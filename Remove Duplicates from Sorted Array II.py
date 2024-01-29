def removeDuplicates(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-1):
            if nums[j] == nums[j+1]:
                if nums[j+i+1] == nums[j+i+2]:
                    nums.pop(nums[j+i+2])





nums = [1,1,1,2,2,3]
print(removeDuplicates(nums))