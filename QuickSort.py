def Qsort(nums):
    if len(nums) <= 1:
        return nums
    l = [x for x in nums[1:] if x <= nums[0]]
    r = [x for x in nums[1:] if x > nums[0]]
    return Qsort(l) + [nums[0]] + Qsort(r)
