from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []

        def dfs(start: int):
            res.append(subset.copy())

            for i in range(start, len(nums)):
                if i != 0 and nums[i] == nums[i - 1]:
                    continue

                subset.append(nums[i])
                dfs(i + 1)
                subset.pop()

        dfs(0)
        return res
