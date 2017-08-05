class solutions(object):
    def rob(self,nums):
        last, now = 0, 0
        for i in nums: last, now = now, max(last+nums[i],now)
        return now
