class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        for i in range(len(arr)):
            if i+1 < len(arr):
                ma = max(arr[i+1:])
            else:
                ma = max(arr[i:])
            arr[i] = ma
        
        arr[-1] = -1

        return arr