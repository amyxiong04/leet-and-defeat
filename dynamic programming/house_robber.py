class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)

        if n == 1:
            return nums[0]

        soln = [0] * n

        if n > 1:
            soln[0] = nums[0]
            soln[1] = max(nums[0], nums[1])

        for i in range(2, n):
            soln[i] = max(soln[i - 1], (soln[i - 2] + nums[i]))
        
        return soln[n - 1]
        