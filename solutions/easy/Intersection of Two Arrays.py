// Title: Intersection of Two Arrays
            // Difficulty: Easy
            // Language: Python
            // Link: https://leetcode.com/problems/intersection-of-two-arrays/

class Solution:
    def intersection(self, nums1, nums2):
        set2 = set(nums2)
        result = set()
        for num in nums1:
            if num in set2:
                result.add(num)
        return list(result)
