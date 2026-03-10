class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if not nums:
            return 0
        
        if n == 1:
            return nums[0]

        def houseRobberI(arr):
            m = len(arr)

            if m == 1:
                return arr[0]
                
            soln = [0] * m
            soln[0] = arr[0]
            soln[1] = max(arr[0], arr[1])

            for i in range(2, m):
                soln[i] = max(soln[i - 1], soln[i - 2] + arr[i])
            
            return soln[m - 1]
        
        # rob either houses index 0 to n - 1 or 1 to n (so that 0 and n never robbed tgt)
        return max(houseRobberI(nums[:-1]), houseRobberI(nums[1:]))