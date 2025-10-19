class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # search space is possible k koko could eat at
        left = 1 # slowest speed
        right = max(piles) # fastest: finish biggest pile in 1 hr
        
        while left <= right:
            speed = (left + right) // 2
            totalTime = 0
            for pile in piles:
                totalTime += ceil(pile / speed)
            if totalTime <= h:
                res = speed # store as candidate min speed
                right = speed - 1 # check is there is a even smaller speed that works
            elif totalTime > h:
                left = speed + 1 # inc speed if can't finish in time
        return res