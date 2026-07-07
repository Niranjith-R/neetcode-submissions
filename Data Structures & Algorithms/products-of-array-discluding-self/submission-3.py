class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        point = 0
        for i in nums:
            count, pro = 0, 1
            while count < len(nums):
                if count == point:
                    count += 1
                else:
                    pro *= nums[count]
                    count += 1
            res.append(pro)
            point += 1
        return res