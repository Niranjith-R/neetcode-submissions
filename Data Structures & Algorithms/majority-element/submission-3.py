class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        half = len(nums)//2
        for i in nums:
            if nums.count(i) >= half:
                return i