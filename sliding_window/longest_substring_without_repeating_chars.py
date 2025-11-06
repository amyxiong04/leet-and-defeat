class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        maxLength = 0
        substring = set()  # current substring w no duplicates

        while right < len(s):
            if s[right] not in substring:
                substring.add(s[right])
                length = right - left + 1
                maxLength = max(maxLength, length)
                right += 1
            else: # remove elements from left from substring until right is not a duplicate of smth already seen
                substring.remove(s[left])
                left += 1

        return maxLength