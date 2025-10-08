# Define Solution with the expected method
class Solution:
    def romanToInt(self, s):
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        prev = 0

        # Traverse from right to left
        for ch in reversed(s):
            val = roman.get(ch)
            if val is None:
                raise ValueError("Invalid Roman numeral character: '{}'".format(ch))
            if val < prev:
                total -= val
            else:
                total += val
            prev = val

        return total


# Example usage / quick test
if __name__ == "__main__":
    print(Solution().romanToInt("III"))      # 3
    print(Solution().romanToInt("IV"))       # 4
    print(Solution().romanToInt("IX"))       # 9
    print(Solution().romanToInt("LVIII"))    # 58
    print(Solution().romanToInt("MCMXCIV"))  # 1994
