class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        print(range(1, n // 2 + 1))
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                print(s[:i])
                pattern = s[:i] * (n // i)
                print(pattern)
                if s == pattern:
                    return True
        return False