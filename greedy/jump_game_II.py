class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0 
        farthest = 0
        currentEnd = 0  # currentEnd keeps track of farthest index you can reach using jumps you already counted 
        n = len(nums)

        for i in range(n-1):
            farthest = max(farthest, i + nums[i])

            if i == currentEnd:  # if at the end of current jump, take another jump 
                jumps += 1
                currentEnd = farthest
            
        return jumps