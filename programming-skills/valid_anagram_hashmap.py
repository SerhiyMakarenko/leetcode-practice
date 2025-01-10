from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        counter_s = Counter(s)
        counter_t = Counter(t)

        if len(s) != len(t):
            return False

        for char in t:
            if char not in counter_s:
                return False

        if counter_s == counter_t:
            return True
        else:
            return False
