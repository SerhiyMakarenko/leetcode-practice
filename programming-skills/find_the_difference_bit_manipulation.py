class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        char = 0

        for char_ in s:
            char ^= ord(char_)

        for char_ in t:
            char ^= ord(char_)

        return chr(char)
