class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}

        for i,v in enumerate(nums):
            pair = target - v 

            if pair in sums:
                return i, sums[pair]

            else:
                sums[v] = i
