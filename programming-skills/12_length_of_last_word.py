class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words_list = s.split()
        return len(words_list[-1])