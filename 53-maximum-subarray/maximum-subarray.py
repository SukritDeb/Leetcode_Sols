class Solution(object):
    def maxSubArray(self, nums):
        e = f = nums[0]

        for i in nums[1:]:
            e = max(i, e + i)
            f = max(f, e)
        
        return f
            