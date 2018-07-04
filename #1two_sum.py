def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
        #========O(N^2)=======================
        #for i in range(0,len(nums)-1):
        #    for j in range(i+1,len(nums)):
        #        if nums[i]+nums[j]==target:
        #            return [i,j]
        #=========O(N)========================
    hash = [-1]*1000000
    for i in range(0, len(nums)):
        if (hash[nums[i]]==-1):
            hash[nums[i]] = i
        else:
            if nums[hash[nums[i]]]+nums[i]==target:
                return [hash[nums[i]],i]
            else:
                hash[nums[i]] = i
    for i in range(0, len(nums)):
        if (nums[i]<=target)or((nums[i]>target)and(nums[i]<0)):
            if (hash[nums[i]]!=-1)and(hash[target - nums[i]]!=-1)and(hash[nums[i]]!=hash[target-nums[i]]):
                return [hash[nums[i]],hash[target-nums[i]]]

#=====main===================

nums = [2,3,4,5,6,7,8,9,10]
target = 19

print(twoSum(nums, target))
