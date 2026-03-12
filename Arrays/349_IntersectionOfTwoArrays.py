# 349. Intersection of Two Arrays
# Problem: https://leetcode.com/problems/intersection-of-two-arrays/
# Submission: https://leetcode.com/problems/intersection-of-two-arrays/submissions/1924655172/

"""
Submission Date: Feb 19, 2026 23:13

Submission Details:
Test Cases Passed: 57 / 57
Runtime: 0 ms (Beats 100.00%)
"""

from ast import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        set1 = set(nums1)
        set2 = set(nums2)
        
        return list(set1 & set2)
