class Solution:
    def isPalindrome(self, s: str) -> bool:


        s = "".join(i for i in s.lower() if i.isalpha() or i.isnumeric())

        a = 0
        b = len(s)-1

        while a <= len(s)/2 and b>=len(s)/2:
            if s[a] == s[b]:
                a+=1
                b-=1
            else:
                return False

        return True