class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        pos = 0 
        for i in nums:
            if i == target:
                return(pos)
                break
            elif i >= target:
                return(pos)
                break
            pos = pos + 1 
        return(len(nums))