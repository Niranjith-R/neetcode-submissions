class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        a = []
        appeared = []
        l = len(nums)
        for i in range(l): 
            if nums[i] in appeared:
                continue
            else:
                appeared.append(nums[i])
            
            count = nums.count(nums[i])
            if count > l / 3 :
                if nums[i] not in a:
                    a.append(nums[i])
        
        if not a:
            return []
        else:
            return a
