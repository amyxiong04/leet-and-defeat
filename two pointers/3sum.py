class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # no duplicate triplets allowed
        
        nums.sort()
        solution = []
        for i, num in enumerate(nums):
            # skip duplicate 'num'
            if i > 0 and num == nums[i - 1]:
                continue
            target = -num
            left = i + 1
            right = len(nums) - 1

            while left < right:
                curr_sum = nums[left] + nums[right]
                if curr_sum < target:
                    left += 1
                elif curr_sum > target:
                    right -= 1
                else:
                    solution.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # skip duplicate left
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # skip duplicate right
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return solution
