class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        left_max = 0
        right_max = 0
        water = 0

        # like container with most water, process left and right sides depending on which one is the limit
        # left_max stores the tallest wall you have passed from the left
        # rihgt_max stores tallest wall you passed from the right
        # when smaller bar appears behind one of those walls, the gap above it holds water 

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1

        return water

