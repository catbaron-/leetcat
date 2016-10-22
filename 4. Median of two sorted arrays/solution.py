# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# Example 1:
#   nums1 = [1, 3]
#   nums2 = [2]
#   The median is 2.0
# Example 2:
#   nums1 = [1, 2]
#   nums2 = [3, 4]
#   The median is (2 + 3)/2 = 2.5

# TODO: improve it to O(log(n+n)) by using binary search
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        p1, p2, cur = 0, 0, 0
        l = len(nums1) + len(nums2)
        even = l % 2
        midle = l / 2
        for i in xrange(midle+even):
            if p1 < len(nums1) and (p2 >= len(nums2) or nums1[p1] < nums2[p2]):
                cur = nums1[p1]
                p1 += 1
            else:
                cur = nums2[p2]
                p2 += 1
        if even == 0:
            if p1 < len(nums1) and (p2 >= len(nums2) or nums1[p1] < nums2[p2]):
                next = nums1[p1]
                p1 += 1
            else:
                next = nums2[p2]
                p2 += 1
            return (cur + next) / 2.0
        else:
            return cur
