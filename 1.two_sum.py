class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prev_diff={}
        for index, value in enumerate(nums):
            diff=target-value
            if diff in prev_diff:
                return [prev_diff[diff],index]
            prev_diff[value]=index
            