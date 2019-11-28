

def solution(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums[i:])):
            if nums[i] + nums[i + j] == target:
                if j != 0:
                    return [i, i + j]
                

nums = [2, 7, 11, 15]
target = 9
print(solution(nums, target))