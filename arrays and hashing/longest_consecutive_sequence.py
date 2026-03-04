class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        nums.sort()
        longest = 1
        current = 1
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:       # consecutive
                current += 1
                longest = max(longest, current)
            elif nums[i] != nums[i-1]:         # reset streak if not duplicate
                current = 1
        
        return longest