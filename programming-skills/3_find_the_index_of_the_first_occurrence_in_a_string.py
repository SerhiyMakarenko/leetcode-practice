class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        h = len(haystack)
        n = len(needle)

        for sliding_window_start in range(h - n + 1):
            print(sliding_window_start)
            for p in range(n):
                print(p)
                if needle[p] != haystack[sliding_window_start + p]:
                    print("The first letter in the needle has the value " + '"' + needle[p] + '"' + ', and it\'s not equal to the first letter in the haystack that has a value ' + '"' + haystack[sliding_window_start + p] + '", moving on...')
                    break
                if p == n - 1:
                    print("The first letter in the needle has the value " + '"' + needle[p] + '"' + ', and it\'s matching the first letter in the haystack that has a value ' + '"' + haystack[sliding_window_start + p] + '". This would be the start of our sliding window!')
                    return sliding_window_start

        print("No mathces found.")
        return -1
