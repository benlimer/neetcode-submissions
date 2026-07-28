class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, val in enumerate(nums):
            diff = target - val
            if val in map.keys():
                return [map[val], i]
            map[diff] = i
