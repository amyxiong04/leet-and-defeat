class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        soln = [0] * n
        soln[0] = nums[0]
        best = soln[0]

        # max subarray for each subarray ending at index i
        for i in range(1, n):
            # find best subarray sum that ends at index i (either start fresh or extend subarray)
            soln[i] = max(nums[i], nums[i] + soln[i - 1])
            best = max(best, soln[i])

        return best
