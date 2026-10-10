# ==========================================================
# 1. Two Sum
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 0 ms (Beats 100%)
# Memory     : 20.5 MB (Beats 43%)
# Link       : https://leetcode.com/problems/two-sum/
# ==========================================================

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Hash map to store the value and its corresponding index
        num_to_index = {}
        
        for index, num in enumerate(nums):
            # Calculate the number needed to reach the target
            complement = target - num
            
            # If the complement is already in the map, we found the solution
            if complement in num_to_index:
                return [num_to_index[complement], index]
            
            # Otherwise, store the current number and its index in the map
            num_to_index[num] = index
