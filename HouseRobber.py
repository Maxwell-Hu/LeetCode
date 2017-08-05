class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return nums[0] if nums else 0
        values = nums[:]
        values[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            values[i] = max(values[i-1],values[i-2]+nums[i])
        return max(values)
