# # Sol1
# def majorityElement(nums):
#     sorted_nums = sorted(nums)
#     n = len(sorted_nums)//2
#     return sorted_nums[n]


# # Sol2
# def majorityElement(nums):
#     nums.sort()
#     return nums[len(nums) // 2]


# # Sol3
# def majorityElement(nums):
#     hash = {}

#     for num in nums:
#         if num not in hash:
#             hash[num] = 1
#         else:
#             hash[num] += 1
    
#     for val, count in hash.items():
#         if count > len(nums) // 2:
#             return val



# # Test
# nums = [2,2,1,1,1,2,2]
# print(majorityElement(nums))