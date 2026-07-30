class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        pref = 1 
        for i in range(len(nums)):
            res[i] = pref
            pref *= nums[i]
        
        # [1, 1, 2, 8]
        postf = 1 
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * postf
            postf *= nums[i]
        
        return res