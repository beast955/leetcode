// Title: Median of Two Sorted Arrays
            // Difficulty: Hard
            // Language: Python
            // Link: https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merged = nums1 + nums2
        merged.sort()
        n = len(merged)
        if n % 2 == 0:
            mid1 = merged[n // 2 - 1]
            mid2 = merged[n // 2]
            return (mid1 + mid2) / 2.0
        else:
            return merged[n // 2]
