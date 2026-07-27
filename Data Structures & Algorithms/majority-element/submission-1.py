class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i not in d.keys():
                d[i] = nums.count(i)
        val  = max(d.values())
        for i in d:
            if d[i] == val:
                return i