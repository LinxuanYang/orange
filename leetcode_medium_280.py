"""
Given an unsorted array nums, reorder it in-place such that
nums[0] <= nums[1] >= nums[2] <= nums[3]....
For example, given nums = [3, 5, 2, 1, 6, 4],
one possible answer is [1, 6, 2, 5, 3, 4].
"""


class Solution(object):
    def wiggle_sort(self, nums):
        nums.sort()
        if len(nums) % 2 != 0:
            #odd number
            for i in range(len(nums)//2):
                nums.insert(i*2+1, nums[len(nums) - 1])
                del nums[len(nums)-1]
        else:
            #even number
            for i in range((len(nums)//2)-1):
                nums.insert(i * 2 + 1, nums[len(nums) - 1])
                del nums[len(nums) - 1]
        return nums


nums = [3, 5, 2, 1, 6, 4, 9]
mysol = Solution()
print(mysol.wiggle_sort(nums))