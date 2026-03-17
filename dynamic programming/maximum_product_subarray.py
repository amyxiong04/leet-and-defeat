# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         # one soln array for max prod so far and one for min prod so far
#         n = len(nums)
#         dp_max = [0] * n
#         dp_min = [0] * n

#         dp_max[0] = nums[0]
#         dp_min[0] = nums[0]

#         res = nums[0]

#         for i in range(1, n):
#             x = nums[i]
            
#             # we need to keep track of min in case it is negative and later if we multiply by another negative it may be max
#             dp_max[i] = max(x * dp_max[i - 1], x * dp_min[i - 1], x)
#             dp_min[i] = min(x * dp_max[i - 1], x * dp_min[i - 1], x)

#             res = max(res, dp_max[i])

#         return res


# condensed version w better runtime and space 
# DP does not require an array.
# DP just means you solve bigger subproblems using smaller subproblems and store/reuse results

from ast import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = nums[0]
        cur_min = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            x = nums[i]

            # this also works
            # if x < 0:
            #     cur_max, cur_min = cur_min, cur_max

            temp = cur_max

            cur_max = max(x, x * temp, x * cur_min)
            cur_min = min(x, x * cur_min, x * temp)

            ans = max(ans, cur_max)

        return ans

            