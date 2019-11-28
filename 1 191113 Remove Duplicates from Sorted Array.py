
def removeDuplicates(nums):
    try:
        prev = nums[0]
        i = 1
        while i != len(nums):
            if nums[i] == prev:
                del nums[i]
            else:
                prev = nums[i]
                i += 1
        return len(nums)
    except:
        return 0


    
a = [0,0,1,1,2,2,2,2,4]
removeDuplicates(a)
