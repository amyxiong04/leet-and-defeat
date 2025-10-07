# solution I came up with
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # dict: num -> frequency
        frequency = {}
        result = []
        for num in nums:
            if num not in frequency:
                frequency[num] = 1
            else:
                frequency[num] += 1
        while k > 0:
            max_key = max(frequency, key=frequency.get)  #.get tells max to compare values instead of keys
            del frequency[max_key]
            result.append(max_key)
            k = k - 1
        return result

# better solution