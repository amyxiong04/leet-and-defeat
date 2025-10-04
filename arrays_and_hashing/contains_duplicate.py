class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

        # set is O(1) accessible bc uses hasing
        # list is O(n) to find a number
        # Time complexity: O(n)