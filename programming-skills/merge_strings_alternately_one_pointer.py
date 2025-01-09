class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        output = ""
        p = 0

        while p < len(''.join([word1, word2])):
            if p < len(word1):
                output += word1[p]
            
            if p < len(word2):
                output += word2[p]
            p += 1

            if p > len(word1):
                output += word1[p:]

            if p > len(word2):
                output += word2[p:]

        return output
