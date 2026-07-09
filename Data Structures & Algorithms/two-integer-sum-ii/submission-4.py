class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a = b = 0
        l = len(numbers)

        while a < l:
            for i in range(a, l):
                if numbers[a] + numbers[i] == target:
                    return [a+1, i+1]
            a += 1
