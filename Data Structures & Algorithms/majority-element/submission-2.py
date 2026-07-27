class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i not in d.values():
                d[nums.count(i)] = i
        val  = max(d.keys())
        return d[val]