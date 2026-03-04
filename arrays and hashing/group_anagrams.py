# hash table
from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = defaultdict(list) # automatically creates ne wlist when key is first seen
        for str in strs:
            letter_count = [0] * 26   # fixed size for a–z
            for char in str:
                letter_count[ord(char) - ord('a')] += 1
            groups[tuple(letter_count)].append(str) # hashable
        return list(groups.values())
    

    # sorting (better)
    class Solution:
        def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            res = defaultdict(list)
            for s in strs:
                sortedS = ''.join(sorted(s))
                res[sortedS].append(s)
            return list(res.values())