def twoSum(nums, target):
    hash = {}

    for i, val in enumerate(nums):
        reminder = target - val
        if reminder in hash:
            return [hash[reminder], i]
        hash[val] = i
        





nums = [2,7,11,15]
target = 9
print(twoSum(nums,target))