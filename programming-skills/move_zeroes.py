class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p = 0

        for n in range(len(nums)):
            if nums[n] != 0:
                nums[n], nums[p] = nums[p], nums[n]
                p += 1