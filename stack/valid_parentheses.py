class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for char in s:
            if char in closeToOpen.values():
                stack.append(char)
            elif char in closeToOpen.keys():
                if not stack or closeToOpen[char] != stack.pop():
                    return False
        return not stack 
