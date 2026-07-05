class Solution:
    def isPalindrome(self, s: str) -> bool:
        sanitized = "".join(char for char in s if char.isalnum())
        a = 0
        b = len(sanitized)-1
        sanitized = sanitized.lower()
        mid = (a+b)/2
        while a <= mid or b >= mid:
            if sanitized[a] != sanitized[b]:
                return False
            else:
                a += 1
                b -= 1
        return True