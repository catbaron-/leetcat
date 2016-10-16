# Given a string, find the length of the longest substring without repeating characters.
# Examples:
# Given "abcabcbb", the answer is "abc", which the length is 3.
# Given "bbbbb", the answer is "b", with the length of 1.
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        index = {}  # cache the position of each char in current sub str
        start = 0   # cache the position of the start char in current sub str
        longest, current = 0, 0 # result, and the length of current sub str
        for i, c in enumerate(s):
            if c in index and index[c] >= start:
                # current c is in current sub str
                # we shuink the current str
                current = current + start - index[c]
                # then update the start position and the index of c
                start = index[c]+1
                index[c] = i
            else:
                # current c is not in current sub str
                # we update the current str, and see if it's longer than
                # the longest sub str
                index[c] = i
                current += 1
                longest = max(longest, current)
        return longest
