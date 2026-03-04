class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        chars_in_s = {}
        chars_in_t = {}
        
        for char in s:
            if char not in chars_in_s:
                chars_in_s[char] = 1
            chars_in_s[char] += 1

        for char in t:
            if char not in chars_in_t:
                chars_in_t[char] = 1
            chars_in_t[char] += 1
        
        return chars_in_t == chars_in_s
    
    # runtime: O(n)