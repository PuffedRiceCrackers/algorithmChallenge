

def solution(nums, target):
    nums_dict = {nums[i]: i for i in range(len(nums))}
    for i in range(len(nums)):
        if nums_dict.get(target - nums[i]) and nums_dict.get(target - nums[i]) != i:
            return [i, nums_dict[target - nums[i]]]
                
nums = [2, 7, 11, 15]
target = 9
print(solution(nums, target))