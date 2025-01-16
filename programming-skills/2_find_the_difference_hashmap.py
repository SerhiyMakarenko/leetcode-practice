from collections import Counter

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        counter_s = Counter(s)

        for char in t:
            if char not in counter_s or counter_s[char] == 0:
                return char
            else:
                counter_s[char] -= 1
