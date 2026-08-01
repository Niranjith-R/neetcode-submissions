class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        l = len(nums)
        a=0

        if nums.count(nums[0]) == len(nums):
            return 1


        while a < len(nums)-1:
            if nums[a] == nums[a+1]:
                nums.pop(a)
                a-=1
            else:
                a += 1
        return len(nums)