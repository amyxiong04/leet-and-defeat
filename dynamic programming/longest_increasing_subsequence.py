class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    # for each i, check every earlier index j from 0 to i - 1 and find max LIS among all valid subsequences that can be extended by nums[i]
                    dp[i] = max(dp[i], dp[j] + 1)
            
        return max(dp)

        