# # solution I came up with
# class Solution(object):
#     def topKFrequent(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: List[int]
#         """
#         # dict: num -> frequency
#         frequency = {}
#         result = []
#         for num in nums:
#             if num not in frequency:
#                 frequency[num] = 1
#             else:
#                 frequency[num] += 1
#         while k > 0:
#             max_key = max(frequency, key=frequency.get)  #.get tells max to compare values instead of keys
#             del frequency[max_key]
#             result.append(max_key)
#             k = k - 1
#         return result

# better solution

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        ans = []

        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            buckets[count].append(num)
        
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
