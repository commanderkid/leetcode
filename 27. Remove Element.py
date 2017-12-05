#Given an array and a value, remove all instances of that value in-place and return the new length.
#Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
#The order of elements can be changed. It doesn't matter what you leave beyond the new length.
#Example:
#Given nums = [3,2,2,3], val = 3,
#Your function should return length = 2, with the first two elements of nums being 2.

def turner(nums, val, chis, i = 0):
    if i <= chis:
        if nums[i] == val:
            nums.pop(i)
            return turner(nums, val, chis - 1, i)  
        else:
            return turner(nums, val, chis, i + 1)
    else:
        return len(nums)


class Solution:
    def removeElement(self, nums, val):
        chis = len(nums) - 1
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        return turner(nums, val, chis)
