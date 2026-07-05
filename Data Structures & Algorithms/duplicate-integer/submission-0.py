class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has_been = []
        for i in nums:
            if i not in has_been:
                has_been.append(i)
            else:
                return True
        return False