
def removeDuplicates(nums):
    dictionary = {}
    iterator = 0
    for i in range(len(nums)):
        if dictionary.get(nums[i]) == None:
            dictionary[nums[i]] = iterator
            iterator += 1
    for k, v in dictionary.items():
        nums[v] = k
    return iterator
    
a = [0,0,1,1,2,2,2,2,4]
length = removeDuplicates(a)
for i in range(length):
    print(a[i])
    