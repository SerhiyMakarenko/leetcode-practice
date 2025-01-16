class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        sorted_arr = sorted(arr)
        d = sorted_arr[1] - sorted_arr[0]
        i = 0
        while i < len(sorted_arr) - 1:
            if sorted_arr[i] + d != sorted_arr[i + 1]:
                return False
            i += 1
        return True