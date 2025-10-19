class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1

        # recursive solution

        # left = 0
        # right = len(nums) - 1

        # def binary_search(left, right):
        #     if left > right:
        #         return -1
        #     while left <= right:
        #         mid = (left + right) // 2
        #         if nums[mid] == target:
        #             return mid
        #         elif nums[mid] < target:
        #             return binary_search(mid + 1, right)
        #         else:
        #             return binary_search(left, mid - 1)
        
        # return binary_search(left, right)
        