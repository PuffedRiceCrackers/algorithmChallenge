def removeElement(nums, val):
    i = 0
    j = len(nums)
    try: 
        if j == 1:
            if nums[0] == val:
                nums.pop()
                return 0
            return 1   
    except:
        return 0
    while i != len(nums) and i < j:
        if nums[i] == val and i < j:  # val 을 발견하면
            j = j if j != len(nums) else j - 1
            while nums[j] == val and i < j:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        i += 1
    count = len(nums) - j
    while count != 0:
        nums.pop()
        count -= 1
    return len(nums)
print(removeElement([], 3))
    

                
            
            



