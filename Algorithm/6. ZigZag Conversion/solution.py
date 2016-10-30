# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
# Subscribe to see which companies asked this question

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or len(s) < 2: return s
        rows = [""]* numRows
        i, right = -1, True
        for ch in s:
            i = i + 1 if right else i - 1
            rows[i] += ch
            # if pointer is pointing to the first or last row, change the direction.
            if i == numRows-1:
                right = False
            if i == 0:
                right = True
        return "".join(rows)
