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
    
        # two pointer method
        #  cleaned = ""
        # for char in s:
        #     if char.isalnum():
        #         cleaned += char.lower()

        # left = 0
        # right = len(cleaned) - 1
        # mid = len(cleaned) / 2

        # while left < mid:
        #     if cleaned[left] != cleaned[right]:
        #         return False
        #     left += 1
        #     right -= 1
        # return True
        