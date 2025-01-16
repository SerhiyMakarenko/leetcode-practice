class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        p = 0
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        while p < len(s):
            if sorted_t[p] != sorted_s[p]:
                return sorted_t[p]
            p += 1

        return sorted_t[p]
