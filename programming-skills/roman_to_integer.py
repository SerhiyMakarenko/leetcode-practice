class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        total = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and roman_numerals[s[i]] < roman_numerals[s[i + 1]]:
                print('This is the subtractive case because pointer i has value ' + str(i) + ", and it's equal to the string symbol " + '"' + s[i] + '".')
                total += roman_numerals[s[i + 1]] - roman_numerals[s[i]]
                i += 2
            else:
                print('This is NOT subtractive case because pointer i has value ' + str(i) + ", and it's equal to the string symbol " + '"' + s[i] + '".')
                total += roman_numerals[s[i]]
                i += 1
            print(total)
        return total