class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indices = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices:
                return [i, indices[diff]]
            indices[n] = i

# using enumerate to keep track of index is O(1)
# time complexity: O(n)