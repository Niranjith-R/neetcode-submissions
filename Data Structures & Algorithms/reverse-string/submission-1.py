class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        a = 0
        b = len(s) - 1

        while a <= len(s)/2 and b >= len(s)/2:
            temp = s[b]
            s[b] = s[a]
            s[a] = temp
            a += 1
            b -= 1