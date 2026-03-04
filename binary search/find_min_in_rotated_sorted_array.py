class Solution:
    def findMin(self, nums: List[int]) -> int:
        # find inflection point using binary search
        left = 0
        right = len(nums) - 1
        res = nums[0] # curr min so far

        while left <= right:
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break
            
            mid = (left + right) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[left]: # this means left half is sorted so min cant be here
                left = mid + 1 # search right side
            else: # nums[mid] < nums[left], so not sorted, search left side
                right = mid - 1
        return res