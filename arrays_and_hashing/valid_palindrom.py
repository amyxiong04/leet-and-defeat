class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        alnumString = ""
        for char in s:
            if char.isalnum():
                alnumString += char
        reversed = alnumString[::-1]
        if alnumString.lower() == reversed.lower():
            return True
        return False
        