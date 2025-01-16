class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = "".join(map(str, digits))
        calculated_digit = int(num) + 1
        return([int(x) for x in str(calculated_digit)])