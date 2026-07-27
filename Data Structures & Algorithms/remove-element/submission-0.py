class Solution:
    def removeElement(self, nums: List, val: int) -> int:
        

        k = len(nums) - nums.count(val)
        count = 0
        while count < len(nums):
            if nums[count] == val:
                nums.pop(count)
            else:
                count +=1
        return k
