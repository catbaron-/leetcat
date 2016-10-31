# Reverse digits of an integer.
# Example1: x = 123, return 321
# Example2: x = -123, return -321

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        m = 1
        if x < 0:
            m = -1
            x = -x
        s = 1
        r = 0
        while s > 0:
            s = x / 10
            r = r * 10 + x % 10
            x = s
        if r > 2147483648:
            r = 0
        r = m*r
        return r
