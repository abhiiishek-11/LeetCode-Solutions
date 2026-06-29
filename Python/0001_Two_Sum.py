# Problem: 0001. Two Sum
# Difficulty: Easy
# Language: Python

class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            needed = target - num

            if needed in seen:
                return [seen[needed], i]

            seen[num] = i