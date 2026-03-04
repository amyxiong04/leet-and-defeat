class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}  # count of chars in window
        maxLength = 0
        left = 0
        maxFreqInWindow = 0 # highest frequency of any char in window
        
        for right in range(len(s)):
            char = s[right]
            freq[char] = freq.get(char, 0) + 1

            # Track the most frequent character count in the current window  
            maxFreqInWindow = max(maxFreqInWindow, freq[char])

            # If window is invalid, shrink from the left
            windowSize = right - left + 1
            neededReplacements = windowSize - maxFreqInWindow

            if neededReplacements > k:
                freq[s[left]] -= 1
                left += 1

            # Update the longest valid window seen so far
            maxLength = max(maxLength, right - left + 1)

        return maxLength