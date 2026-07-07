class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        map = {}
        for i in nums:
            map[i] = nums.count(i)

        res = []
    
        arr = sorted(list(map.items()), key = lambda x: x[1])

        for i in range(len(arr)):
            if i == k:
                break
            else:
                res.append(arr[-1][0])
                arr.pop()


        return res